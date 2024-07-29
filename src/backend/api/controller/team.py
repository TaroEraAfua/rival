# coding: utf-8
import datetime
import base64
import json
import os
import api.common.unit as format
import api.common.constant as constant
from api.model.team import Team
from api.common.sql import team_sql_format, search_team_format
from api.common.unit import debug_log


def get_from_detail(team_id, user_id, prefecture_id, city_id, station_id,
                    line_id, gender, purpose_list, week_list, page):
    # チーム検索　詳細情報
    response = None
    try:
        select_sql, from_sql = team_sql_format(team_id, user_id=user_id)
        where_sql = search_team_format(prefecture_id=prefecture_id, city_id=city_id,
                                       station_id=station_id, line_id=line_id, gender=gender, purpose_list=purpose_list,
                                       week_list=week_list)
        offset = make_offset(page)
        team_list, counter = Team.get_team_list(select_sql, from_sql, where_sql, offset)
        res_team = format.convert_team_data(team_list, team_id, True)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            {
                'prof': res_team,
                'count': counter,
            }
        )
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def get_from_game_date(team_id, user_id, date_list, prefecture_id, city_id, station_id, line_id, page):
    debug_log('get_from_game_date')
    response = None
    try:
        select_sql, from_sql = team_sql_format(team_id, user_id=user_id)
        where_sql = search_team_format(prefecture_id=prefecture_id, city_id=city_id,
                                       station_id=station_id, date_list=date_list, line_id=line_id)
        offset = make_offset(page)
        team_list, counter = Team.get_team_list(select_sql, from_sql, where_sql, offset)

        res_team = format.convert_team_data(team_list, team_id, True)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            {
                'prof': res_team,
                'count': counter,
            }
        )
    except Exception as e:
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def add_account(team_id, user_id, admin, team_name, image_data, image_name, prefecture, city,
                station, gender, purpose, game_date, gym, main_place, feature, average_age,
                member_num, stray_flg, solicitation, c_comment, u_comment):
    debug_log('add_account')
    response = None
    try:
        debug_log("１")
        c_path = os.path.dirname(os.path.abspath(__file__))
        o_path = os.path.abspath(c_path + '../../../storage/images/' + user_id + '/' + team_id)
        debug_log("２")
        if image_name == '':
            i_path = os.path.abspath(c_path + '../../icon/noImage.jpg')
        else:
            now = datetime.datetime.now()
            i_path = o_path + '/' + team_id + '_' + now.strftime('%Y%m%d%H%M%S') + '.jpg'

        to_day = datetime.datetime.today()
        register_dt = to_day.strftime("%Y-%m-%d")
        update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")
        debug_log("３")
        p_info = format.format_team_info(team_id, user_id, admin, register_dt, update_time)

        # p_week = format.format_t_week(team_id, week, register_dt, update_time)
        debug_log("４")
        p_purpose = format.format_t_purpose(team_id, purpose, register_dt, update_time)
        debug_log("５")

        p_feature = format.format_t_feature(team_id, feature, register_dt)
        debug_log("６")
        p_prof = format.format_team_profile(team_id, team_name, i_path, prefecture, city,
                                            station, gender, gym, average_age, solicitation, stray_flg,
                                            main_place, member_num, c_comment, u_comment, register_dt, update_time)
        debug_log("７")
        result = Team.set_team(user_id, p_info, p_prof, p_purpose, p_feature)
        debug_log("８")
        # 何も戻ってこない時(True)は正常終了 'err'(False)はエラー
        if result is None:

            if '' != image_data:
                if ';base64,' in image_data:
                    image_data = image_data.split(';base64,')[1]
                os.makedirs(o_path, exist_ok=True)
                with open(i_path, "wb") as f:
                    f.write(base64.b64decode(image_data))
            code = constant.RESULT_CODE_OK
            message = constant.MESSAGE_OK_001
        else:
            Team.delete_team_account(team_id)
            code = constant.RESULT_CODE_ERR
            message = result['message']
        response = format.format_return_param(code, message)
    except Exception as e:
        debug_log(e)
        Team.delete_team_account(team_id)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    debug_log(response)
    return response


def update_team_profile(team_id, user_id, admin, team_name, image_data, image_name, prefecture, city,
                        station, gender, purpose, game_date, gym, main_place, feature, average_age,
                        member_num, stray_flg, solicitation, c_comment, u_comment):
    try:
        c_path = os.path.dirname(os.path.abspath(__file__))
        o_path = os.path.abspath(c_path + '../../../storage/images/' + user_id + '/' + team_id)
        if image_name == '':
            i_path = os.path.abspath(c_path + '../../icon/noImage.jpg')
        else:
            now = datetime.datetime.now()
            i_path = o_path + '/' + team_id + '_' + now.strftime('%Y%m%d%H%M%S') + '.jpg'

        to_day = datetime.datetime.today()
        register_dt = to_day.strftime("%Y-%m-%d")
        update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")

        # p_info = format.format_team_info(team_id, user_id, admin, register_dt, update_time)
        # p_week = format.format_t_week(team_id, week, register_dt, update_time)

        p_purpose = format.format_t_purpose(team_id, purpose, register_dt, update_time)

        p_game_date = format.format_t_game_date(team_id, game_date, register_dt, update_time)

        p_feature = format.format_t_feature(team_id, feature, register_dt)

        p_prof = format.format_team_profile(team_id, team_name, i_path, prefecture, city,
                                            station, gender, gym, average_age, solicitation, stray_flg,
                                            main_place, member_num, c_comment, u_comment, register_dt, update_time)

        # p_member = format.format_t_member(team_id, member, register_dt, update_time)
        result = Team.update_team_profile(team_id, p_prof, p_purpose, p_feature, p_game_date)
        # 何も戻ってこない時(True)は正常終了 'err'(False)はエラー
        if result is None:
            if '' != image_data:
                if ';base64,' in image_data:
                    image_data = image_data.split(';base64,')[1]
                os.makedirs(o_path, exist_ok=True)
                with open(i_path, "wb") as f:
                    f.write(base64.b64decode(image_data))
            code = constant.RESULT_CODE_OK
            message = constant.MESSAGE_OK_001
        else:
            code = constant.RESULT_CODE_ERR
            message = result['message']
        response = format.format_return_param(code, message)
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def update_team_game_date(team_id, game_date):
    debug_log('update_team_game_date')
    try:
        to_day = datetime.datetime.today()
        register_dt = to_day.strftime("%Y-%m-%d")
        update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")
        game = format.format_t_game_date(team_id, game_date, register_dt, update_time)
        debug_log(game)
        result = Team.update_team_game_date(team_id, game)
        # 何も戻ってこない時(True)は正常終了 'err'(False)はエラー
        if result is None:
            code = constant.RESULT_CODE_OK
            message = constant.MESSAGE_OK_001
        else:
            code = constant.RESULT_CODE_ERR
            message = result['message']
        response = format.format_return_param(code, message)

    except Exception as e:
        debug_log("Exception")
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def update_team_info(team_id, user_id, admin):
    try:
        to_day = datetime.datetime.today()
        register_dt = to_day.strftime("%Y-%m-%d")
        update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")
        p_info = format.format_team_info(team_id, user_id, admin, register_dt, update_time)
        result = Team.update_team_info(p_info)
        # 何も戻ってこない時(True)は正常終了 'err'(False)はエラーを返却
        if result is None:
            code = constant.RESULT_CODE_OK
            message = constant.MESSAGE_OK_001
        else:
            code = constant.RESULT_CODE_ERR
            message = result['message']
        response = format.format_return_param(code, message)

    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def delete_team_info(team_id, user_id):
    try:
        result = Team.delete_team_info(team_id, user_id)
        # 何も戻ってこない時(True)は正常終了 'err'(False)はエラー
        if result is None:
            code = constant.RESULT_CODE_OK
            message = constant.MESSAGE_OK_001
        else:
            code = constant.RESULT_CODE_ERR
            message = result['message']
        response = format.format_return_param(code, message)

    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def check_team_id(team_id):
    # team_id　有無確認
    result = Team.check_info(team_id)
    return result.to_dict_team_info()


def add_team_user(team_id, user_id, status, comment):
    try:
        to_day = datetime.datetime.today()
        send = {
            'team_id': team_id,
            'user_id': user_id,
            'status': status,
            'register_dt': to_day.strftime("%Y-%m-%d"),
        }
        result = Team.add_team_user(send)
        if result is None:
            code = constant.RESULT_CODE_OK
            message = constant.MESSAGE_OK_001
        else:
            code = constant.RESULT_CODE_ERR
            message = result['message']
        response = format.format_return_param(code, message)

    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def get_team_profile(team_id, user_id):
    try:
        send = {
            'team_id': team_id,
            'user_id': user_id,
        }
        result = Team.get_team(send)
        if result is not None:
            code = constant.RESULT_CODE_OK
            message = constant.MESSAGE_OK_001
            data = format.convert_team_data(result)
        else:
            code = constant.RESULT_CODE_ERR
            message = result['message']
            data = result
        response = format.format_return_param(code, message, data)
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def make_offset(page):
    # ページ計算
    offset = (page - 1) * 20
    return offset
