# coding: utf-8
import datetime
from api.model.schedules import Schedule
from api.common.constant import RESULT_CODE_OK, RESULT_CODE_ERR, MESSAGE_OK_001, MESSAGE_ERR_007
from api.util.logging import Logger
import json
import sys
import os
import base64
import api.common.unit as format
import api.common.constant as constant
from sqlalchemy.exc import SQLAlchemyError

from api.model.team import Team
from api.model.user import User
from api.common.sql import team_sql_format, search_team_format
from api.common.unit import convert_team_data, convert_user_data, format_return_param
from api.model.const import Const

from api.common.unit import debug_log


def get_user(user_id):
    select_sql, from_sql = team_sql_format(user_id=user_id, search_flg=False)
    where_sql = search_team_format(user_id=user_id)
    try:
        user_list = User.get_user_prof(user_id)
        # Exception時は返却する
        if type(user_list) == dict:
            if 'err' in user_list.keys():
                debug_log(user_list)
                response = format.format_return_param(
                    constant.RESULT_CODE_ERR_SYSTEM,
                    constant.MESSAGE_ERR_SYSTEM
                )

        res_user = convert_user_data(user_list)
        team_list, counter = Team.get_team_list(select_sql, from_sql, where_sql, t_flg=False)

        res_team = []
        if len(team_list) > 0:
            team_id = team_list[0].to_dict_team_info()["team_id"]
            res_team = convert_team_data(team_list, team_id, False)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            {'user': res_user, 'team': res_team}
        )

    except Exception as e:
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    debug_log(response)
    return response


def create_schedule(user_id, title, description, start_time, end_time):
    logger = Logger()
    try:
        # Validate user_id
        user = check_user(user_id)
        if not user:
            return format.format_return_param(RESULT_CODE_ERR, "Invalid user_id")

        # Validate datetime format and logical correctness
        try:
            start_dt = datetime.datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
            end_dt = datetime.datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
            if start_dt >= end_dt:
                return format.format_return_param(RESULT_CODE_ERR, "start_time must be before end_time")
        except ValueError:
            return format.format_return_param(RESULT_CODE_ERR, "Invalid datetime format")

        # Check for conflicting schedules
        if Schedule.check_conflicts(user_id, start_dt, end_dt):
            return format.format_return_param(RESULT_CODE_ERR, MESSAGE_ERR_007)

        # Create new schedule entry
        new_schedule = Schedule(
            title=title,
            description=description,
            start_time=start_dt,
            end_time=end_dt,
            register_dt=datetime.datetime.utcnow(),
            update_time=datetime.datetime.utcnow(),
            user_id=user_id
        )
        new_schedule.save()

        # Log the creation of the new schedule
        logger.info(f"New schedule created for user_id {user_id} with title {title}")

        return format.format_return_param(RESULT_CODE_OK, MESSAGE_OK_001)
    except SQLAlchemyError as e:
        logger.error('SQLAlchemyError', str(e))
        return format.format_return_param(RESULT_CODE_ERR, "Database error occurred")
    except Exception as e:
        logger.error('Exception', str(e))
        return format.format_return_param(RESULT_CODE_ERR_SYSTEM, "An unexpected error occurred")


def check_user(user_id):
    # 有無確認 errはdictなのでそのまま返す
    # 正常終了時はdict変換後返却（None時はそのまま）
    user = User.check_user(user_id)
    return user


# ...rest of the code remains unchanged...

# Add other user controller methods below