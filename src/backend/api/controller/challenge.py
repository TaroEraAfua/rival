# coding: utf-8
import datetime
import base64
import json
from api.model.challenge import Challenge
from api.model.team import Team
import api.common.unit as format
import api.common.constant as constant

from api.common.sql import team_sql_format, search_team_format
from api.common.unit import convert_team_data
from api.common.unit import debug_log


def set_challenge(send_id, res_id, game_date, game_time_start):
    debug_log('set_challenge')
    try:
        challenge = format.format_challenge(send_id, res_id, game_date, game_time_start, 0)
        res = Challenge.set_challenge(challenge)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            res
        )
    except Exception as e:
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    debug_log(response)
    return response


def change_challenge_status(challenge_id, status=0):
    try:

        to_day = datetime.datetime.today()
        update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")
        challenge = {
            'challenge_id': challenge_id,
            'challenge_status': status,
            'update_time': update_time
        };
        res = Challenge.update_challenge(challenge)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            res
        )
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def delete_challenge(challenge_id):
    try:
        res = Challenge.del_challenge(challenge_id)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            res
        )
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def get_challenge(team_id):
    try:
        select_sql, from_sql = team_sql_format(team_id=team_id)
        where_sql = search_team_format(team_id=team_id)
        team_list, counter = Team.get_team_list(select_sql, from_sql, where_sql, t_flg=False)
        con_team = convert_team_data(team_list, team_id=team_id)
        data = None
        if len(con_team) > 0:
            res_list = []
            match_list = []
            send_list = []
            for row in con_team:

                if row['team_id'] != team_id and row['game_date'] is not None:
                    debug_log("aaa")
                    for idx, game in enumerate(row['game_date']):
                        tmp = row.copy()
                        debug_log(idx)
                        tmp['game_date'] = [row['game_date'][idx]]
                        if game['exec_type'] == 'MATCH':
                            debug_log(tmp['game_date'])
                            match_list.append(tmp)
                        elif game['exec_type'] == 'SEND':
                            send_list.append(tmp)
                        elif game['exec_type'] == 'RES':
                            res_list.append(tmp)
            data = {'RES': res_list, 'SEND': send_list, 'MATCH': match_list}
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            data
        )
    except Exception as e:
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def get_team(team_id):
    try:
        select_sql, from_sql = team_sql_format(team_id=team_id)
        where_sql = search_team_format(team_id=team_id)
        team_list, counter = Team.get_team_list(select_sql, from_sql, where_sql, t_flg=False)
        con_team = convert_team_data(team_list, team_id)

        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            con_team
        )
    except Exception as e:
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response