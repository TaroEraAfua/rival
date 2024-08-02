# coding: utf-8
import datetime
from api.model.schedules import Schedule
import json
import sys
import os
import base64
import api.common.unit as format
import api.common.constant as constant

from api.model.team import Team
from api.model.user import User
from api.common.sql import team_sql_format, search_team_format
from api.common.sql import check_schedule_conflict
from api.common.unit import convert_team_data, convert_user_data, format_return_param
from api.model.const import Const
from api.common.unit import debug_log
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from api.common.database import db_session
from api.util.logging import Logger


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


def check_user(user_id):
    # 有無確認 errはdictなのでそのまま返す
    # 正常終了時はdict変換後返却（None時はそのまま）
    user = User.check_user(user_id)
    return user


def sign_in(user_id, password):
    try:
        to_day = datetime.datetime.today()
        param = {
            'user_id': user_id,
            'sign_in_time': to_day.strftime("%Y-%m-%d %H:%M:%S"),
            'update_time': to_day.strftime("%Y-%m-%d %H:%M:%S"),
        }
        user = User.check_user(user_id)
        if user is None:
            response = format.format_return_param(
                constant.RESULT_CODE_ERR,
                constant.MESSAGE_ERR_004
            )
        elif user.password == password:
            User.sign_in(param)
            res = get_user(user_id)
            if 'err' in res:
                response = format.format_return_param(
                    constant.RESULT_CODE_ERR_SYSTEM,
                    constant.MESSAGE_ERR_SYSTEM
                )
            else:
                response = format.format_return_param(
                    constant.RESULT_CODE_OK,
                    constant.MESSAGE_OK_001,
                    {'user': res['data']['user'], 'team': res['data']['team']}
                )

        else:
            response = format.format_return_param(
                constant.RESULT_CODE_ERR,
                constant.MESSAGE_ERR_004
            )

    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def update_pass(user_id, password_old, password_new):
    try:
        to_day = datetime.datetime.today()
        user = User.check_user(user_id)
        if user.password == password_old:
            # 旧パスワードと同一のパスワードはエラー
            if user.password == password_new:
                response = format.format_return_param(
                    constant.RESULT_CODE_ERR,
                    constant.MESSAGE_ERR_003
                )
            else:
                # 旧パスワードでなければパスワードを更新
                param = {
                    'user_id': user_id,
                    'password': password_new,
                    'update_time': to_day.strftime("%Y-%m-%d %H:%M:%S"),
                }
                data = User.update_user_pass(param)
                response = format.format_return_param(
                    constant.RESULT_CODE_OK,
                    constant.MESSAGE_OK_001,
                    data
                )
        else:
            response = format.format_return_param(
                constant.RESULT_CODE_ERR,
                constant.MESSAGE_ERR_005
            )

    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def add_user(user_id, user_name, password, prefecture, city,
             gender, birth_dt, mail, image_name, image_data, height, position, ex_year, ex_width, comment):
    try:
        c_path = os.path.dirname(os.path.abspath(__file__))
        o_path = os.path.abspath(c_path + '../../../storage/images/' + user_id)
        if image_name == '':
            i_path = os.path.abspath(c_path + '../../icon/noImage.jpg')
        else:
            now = datetime.datetime.now()
            i_path = o_path + '/' + user_id + '_' + now.strftime('%Y%m%d%H%M%S') + '.jpg'

            debug_log(i_path)
        check = check_user(user_id)
        if check is None:
            to_day = datetime.datetime.today()
            register_dt = to_day.strftime("%Y-%m-%d")
            update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")
            p_user = format.format_user_info(user_id, user_name, birth_dt, prefecture,
                                             city, gender, register_dt, update_time,
                                             ex_year, height, comment, i_path, mail, password)
            p_position = format.format_user_position(user_id, position, register_dt, update_time)
            p_u_width = format.format_user_width(user_id, ex_width, register_dt)
            # p_week = format.format_u_week(user_id, week, register_dt, update_time)

            data = User.set_user_info(user_id, p_user, p_u_width, p_position)

            if data is None:
                if '' != image_data:
                    if ';base64,' in image_data:
                        image_data = image_data.split(';base64,')[1]
                    os.makedirs(o_path, exist_ok=True)
                    with open(i_path, "wb") as f:
                        f.write(base64.b64decode(image_data))
                        debug_log(image_data)
                code = constant.RESULT_CODE_OK
                message = constant.MESSAGE_OK_001
            else:
                User.delete_user_account(user_id)
                code = constant.RESULT_CODE_ERR
                message = data['message']

            response = format.format_return_param(code, message)

        else:
            User.delete_user_account(user_id)
            response = format.format_return_param(
                constant.RESULT_CODE_ERR,
                constant.MESSAGE_ERR_001
            )

    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def update_user(user_id, user_name, prefecture, city, gender, birth_dt, mail,
                image_name, image_data, height, position, ex_year, ex_width, comment):
    try:
        c_path = os.path.dirname(os.path.abspath(__file__))
        o_path = os.path.abspath(c_path + '../../../storage/images/' + user_id)
        if image_name == '':

            i_path = os.path.abspath(c_path + '../../icon/noImage.jpg')
        else:
            now = datetime.datetime.now()
            i_path = o_path + '/' + user_id + '_' + now.strftime('%Y%m%d%H%M%S') + '.jpg'

            debug_log(i_path)

        to_day = datetime.datetime.today()
        register_dt = to_day.strftime("%Y-%m-%d")
        update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")
        p_user = format.format_user_info(user_id, user_name, birth_dt, prefecture,
                                         city, gender, register_dt, update_time,
                                         ex_year, height, comment, i_path, mail)
        p_position = format.format_user_position(user_id, position, register_dt, update_time)
        p_u_width = format.format_user_width(user_id, ex_width, register_dt)
        # p_week = format.format_u_week(user_id, week, register_dt, update_time)

        data = User.set_user_info(user_id, p_user, p_u_width, p_position)

        if data is None:
            if '' != image_data:
                if ';base64,' in image_data:
                    image_data = image_data.split(';base64,')[1]
                os.makedirs(o_path, exist_ok=True)
                with open(i_path, "wb") as f:
                    f.write(base64.b64decode(image_data))
                    debug_log(image_data)
            code = constant.RESULT_CODE_OK
            message = constant.MESSAGE_OK_001
        else:
            code = constant.RESULT_CODE_ERR
            message = data['err']

        response = format.format_return_param(code, message)
    except Exception as e:
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response

def check_favorite_team(user_id, team_id):
    to_day = datetime.datetime.today()
    register_dt = to_day.strftime("%Y-%m-%d")
    update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")

    param = {
        'user_id': user_id,
        'team_id': team_id,
        'register_dt': register_dt,
        'update_time': update_time,
    }

    result = User.check_favorite_team(param)
    return result

def update_schedule(schedule_id, user_id, title, description, start_time, end_time):
    try:
        # Validate schedule_id and user_id
        schedule = db_session.query(Schedule).filter_by(schedule_id=schedule_id, user_id=user_id).first()
        if not schedule:
            return format_return_param(constant.RESULT_CODE_ERR, "Invalid schedule_id or user_id")

        # Validate start_time and end_time
        if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
            return format_return_param(constant.RESULT_CODE_ERR, "Invalid datetime format")
        if start_time >= end_time:
            return format_return_param(constant.RESULT_CODE_ERR, "start_time must be before end_time")

        # Check for conflicting schedules
        if check_schedule_conflict(user_id, start_time, end_time, schedule_id):
            return format_return_param(constant.RESULT_CODE_ERR, "Conflicting schedule exists")

        # Update the schedule
        schedule.title = title
        schedule.description = description
        schedule.start_time = start_time
        schedule.end_time = end_time
        schedule.update_time = datetime.datetime.utcnow()
        db_session.commit()

        # Log the update action
        logger = Logger()
        logger.audit_log(datetime.datetime.utcnow(), user_id, schedule_id, "Schedule updated")

        return format_return_param(constant.RESULT_CODE_OK, "Schedule updated successfully")
    except Exception as e:
        db_session.rollback()
        debug_log(e)
        return format_return_param(constant.RESULT_CODE_ERR_SYSTEM, constant.MESSAGE_ERR_SYSTEM)

# Helper function to check for schedule conflicts
def check_schedule_conflict(user_id, start_time, end_time, exclude_schedule_id=None):
    # This function should check for any schedules that overlap with the given time range
    # excluding the schedule with exclude_schedule_id if provided.
    # For simplicity, we assume the function exists in sql.py and returns True if a conflict exists.
    return db_session.query(Schedule).filter(
        Schedule.user_id == user_id,
        Schedule.end_time > start_time,
        Schedule.start_time < end_time,
        Schedule.schedule_id != exclude_schedule_id
    ).count() > 0