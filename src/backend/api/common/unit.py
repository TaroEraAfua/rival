# coding: utf-8
import base64
import datetime
import json
import api.common.sql as format
from api.model.team import Team
from api.model.challenge import Challenge
from api.model.const import Const
import util.logging as LOGGER
import os
import sys
import io
from logging import getLogger, StreamHandler, DEBUG, Formatter, FileHandler, handlers
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

error_logger = LOGGER.Logger('error.log', 'error')
system_error_logger = LOGGER.Logger('systemError.log', 'systemError')


def convert_user_data(user_list):
    debug_log('convert_user_data')
    result = {}
    cnt = 0
    for row in user_list:
        debug_log(row)
        cnt += 1
        user = row.to_dict()

        if 'user_id' in result.keys():
            tmp = result
            if user['week_id'] not in tmp['week'].keys():
                result['week'][user['week_id']] = [user['time_id']]

            elif user['time_id'] not in tmp['week'][user['week_id']]:
                result['week'][user['week_id']].append(user['time_id'])

            if user["position_id"] not in tmp["position"]:
                result['position'].append(user["position_id"])

            if user['width_id'] not in tmp["ex_width"]:
                result['ex_width'].append(user["width_id"])

        else:
            t = user['icon']
            with open(t, "rb") as f:
                user['icon'] = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')
            result = {
                'user_id': user['user_id'],
                'user_name': user['user_name'],
                'prefecture': {'key': user['prefecture_id'], 'val': user['prefecture_name']},
                'city': {'key': user['city_id'] , 'val': user['city_name']},
                # 'line': {user['line_id']: user['line_name']},
                # 'station': {user['station_id']: user['station_name']},
                'icon': user['icon'],
                'birth_dt': user['birth_dt'].strftime("%Y/%m/%d"),
                'gender': user['gender'],
                "week": {user['week_id']: [user['time_id']]},
                "position": [user['position_id']],
                "ex_year": user['ex_year'],
                "height": user['height'],
                "ex_width": [user['width_id']],
                "message": user["message"]
            }
    return result


def convert_team_data(team_list, team_id="", search_flg=False):
    debug_log('convert_team_data start')
    result = {}
    g_list = {}
    w_list = {}
    p_list = {}
    f_list = {}
    debug_log('convert_team_data 00')
    if team_list:
        w_sql = format.team_format(team_list)
        debug_log('convert_team_data 0')
        # wc_sql = format.challenge_team_format(team_list)
        game_date = Team.get_game_date(team_id, w_sql, search_flg)
        debug_log('convert_team_data 1')
        challenge = Challenge.get_challenge_state(team_id)
        debug_log('convert_team_data 2')
        feature = Team.get_feature(w_sql)
        purpose = Team.get_purpose(w_sql)
        debug_log("game_date")
        for row in game_date:
            d = row.to_dict_game_date()
            row = {
                "game_date": d['game_date'].strftime("%Y/%m/%d"),
                "game_time_start": str(d['game_time_start']),
                "game_time_end": str(d['game_time_end']) if d['game_time_end'] else None,
                "challenge_id": d['challenge_id'],
                "exec_type": d['exec_type'],
                "comment": d['comment'],
            }
            if d['team_id'] in g_list.keys():
                g_list[d['team_id']].append(row)
            else:
                g_list[d['team_id']] = [row]

        for row in challenge:
            d = row.to_dict()
            row = {
                "game_date": d['game_date'].strftime("%Y/%m/%d"),
                "game_time_start": str(d['game_time_start']),
                "game_time_end": str(d['game_time_end']) if d['game_time_end'] else None,
                "challenge_id": d['challenge_id'],
                "exec_type": d['exec_type'],
                "comment": d['comment'],
            }
            if d['send_team_id'] in g_list.keys():
                g_list[d['send_team_id']].append(row)
            else:
                g_list[d['send_team_id']] = [row]

        debug_log("feature")
        for row in feature:
            d = row.to_dict_feature()
            debug_log(d)
            if d['team_id'] in f_list.keys():
                f_list[d['team_id']].append(d['feature_id'])
            else:
                f_list[d['team_id']] = [d['feature_id']]
        debug_log("purpose")
        for row in purpose:
            d = row.to_dict_purpose()
            if d['team_id'] in p_list.keys():
                p_list[d['team_id']].append(int(d['purpose_id']))
            else:
                p_list[d['team_id']] = [int(d['purpose_id'])]

        for row in team_list:
            team = row.to_dict_team_info()
            img = None
            row
            if team['team_image'] is not None:
                # base64でencode
                tag = 'png'
                if '.png'in team['team_image'][-4:].lower():
                    tag = 'png'
                elif '.jpg' in team['team_image'][-4:].lower() or '.jpeg' in team['team_image'][-4:].lower():
                    tag = 'jpg'
                elif '.gif' in team['team_image'][-4:].lower():
                    tag = 'gif'
                elif '.bmp' in team['team_image'][-4:].lower():
                    tag = 'bmp'
                with open(team['team_image'], "rb") as f:
                    img = 'data:image/' + tag + ';base64,' + base64.b64encode(f.read()).decode('utf-8')

            result[team['team_id']] = {
                'team_id': team['team_id'],
                'team_name': team['team_name'],
                'team_image': img,
                'admin': team['admin'],
                'prefecture': {'key': team['prefecture_id'], 'val': team['prefecture_name']},
                'city': {'key': team['city_id'] , 'val': team['city_name']},
                'line': {'key': team['line_id'], 'val': team['line_name']},
                'station': {'key': team['station_id'], 'val': team['station_name']},
                'gender': team['gender'],
                'c_comment': team['c_comment'],
                'u_comment': team['u_comment'],
                'main_place': team['main_place'],
                'average_age': team['avg_age'],
                'gym': team['gym'],
                'solicitation': team['solicitation_flg'],
                'member_num': team['member_num'],
                'stray_flg': team['stray_flg'],
                'status': team['status'],
                'feature': f_list[team['team_id']] if team['team_id'] in f_list.keys() else None,
                'game_date': g_list[team['team_id']] if team['team_id'] in g_list.keys() else None,
                'purpose': p_list[team['team_id']] if team['team_id'] in p_list.keys() else None,
            }
    prof = []
    debug_log('convert_team_data end')
    for val in result.values():
        prof.append(val)
    return prof


def format_team_info(team_id, user_id, admin, register_dt, update_time):
    p_info = {
        'team_id': team_id,
        'user_id': user_id,
        'admin': admin,
        'register_dt': register_dt,
        'update_time': update_time
    }
    return p_info


def format_team_profile(team_id, team_name, image_path, prefecture, city, station, gender,
                        gym, average_age, solicitation, stray_flg, main_place, member_num, c_comment,
                        u_comment, register_dt, update_time):
    p_prof = {
        'team_id': team_id,
        'team_name': team_name,
        'team_image': image_path,
        'prefecture_id': prefecture,
        'city_id': city,
        'line_id': station['line_id'],
        'station_id': station['station_id'],
        'gender': gender,
        'gym': gym,
        'avg_age': average_age,
        'solicitation_flg': solicitation,
        'stray_flg': stray_flg,
        'main_place': main_place,
        'member_num': member_num,
        'c_comment': c_comment,
        'u_comment': u_comment,
        'register_dt': register_dt,
        'update_time': update_time
    }
    return p_prof


def format_t_week(team_id, week, register_dt, update_time):
    p_week = []
    for week_id, times in week.items():
        for time_id in times:
            tmp = (team_id, week_id, time_id, register_dt, update_time)
            p_week.append(tmp)
    return p_week


def format_t_purpose(team_id, purpose, register_dt, update_time):
    p_purpose = []
    for row in purpose:
        tmp = {
            'team_id': team_id,
            'purpose_id': row,
            'register_dt': register_dt,
            'update_time': update_time,
        }
        p_purpose.append(tmp)
    return p_purpose


def format_t_game_date(team_id, game_date, register_dt, update_time):
    p_game_date = []
    for g_date in game_date:
        tmp = {
            'team_id': team_id,
            'game_date': g_date['game_date'],
            'game_time_start': g_date["game_time_start"],
            'game_time_end': g_date["game_time_end"],
            'comment': g_date["comment"],
            'register_dt': register_dt,
            'update_time': update_time,
        }
        p_game_date.append(tmp)
    return p_game_date


def format_t_member(team_id, member, register_dt, update_time):
    p_member = []
    for key, val in member.items():
        tmp = {
            'team_id': team_id,
            'mem_level_id': key,
            'mem_num': val,
            'register_dt': register_dt,
            'update_time': update_time,
        }
        p_member.append(tmp)
    return p_member


def format_t_feature(team_id, feature, register_dt):
    p_feature = []
    for feature_id in feature:
        tmp = {
            'team_id': team_id,
            'feature_id': feature_id,
            'register_dt': register_dt,
        }
        p_feature.append(tmp)

    return p_feature


def format_user_info(user_id, user_name, birth_dt, prefecture,
                     city, gender, register_dt, update_time, ex_year, height, comment, icon, mail, password=""):
    result = {
        'user_id': user_id,
        'password': password,
        'user_name': user_name,
        'mail': mail,
        'birth_dt': birth_dt[0:10],
        'prefecture_id': prefecture,
        'sign_in_time': None,
        'city_id': city,
        'gender': gender,
        'ex_year': ex_year,
        'height': height,
        'comment': comment,
        'register_dt': register_dt,
        'update_time': update_time,
        'icon': icon
    }
    return result


def format_user_width(user_id, ex_width, register_dt):
    result = []
    for width_id in ex_width:
        tmp = {
            'user_id': user_id,
            'width_id': width_id,
            'register_dt': register_dt,
        }
        result.append(tmp)
    return result


def format_user_position(user_id, position, register_dt, update_time):
    result = []
    for position_id in position:
        tmp = {
            'user_id': user_id,
            'position_id': position_id,
            'register_dt': register_dt,
            'update_time': update_time,
        }
        result.append(tmp)
    return result


def format_u_week(user_id, week, register_dt, update_time):
    p_week = []
    for week_id, times in week.items():
        for time_id in times:
            tmp = {
                'user_id': user_id,
                'week_id': week_id,
                'time_id': time_id,
                'register_dt': register_dt,
                'update_time': update_time,
            }
            p_week.append(tmp)
    return p_week


def format_challenge(send_id, team_id, game_date, game_time_start, status=0):
    to_day = datetime.datetime.today()
    challenge_id = send_id + team_id + game_date + game_time_start.replace('/', '').replace(':', '') + to_day.strftime("%Y%m%d")
    register_dt = to_day.strftime("%Y-%m-%d")
    update_time = to_day.strftime("%Y-%m-%d %H:%M:%S")
    challenge = {
        'challenge_id': challenge_id,
        'send_team_id': team_id,
        'team_id': send_id,
        'game_date': game_date,
        'game_time_start': game_time_start,
        'challenge_status': status,
        'register_dt': register_dt,
        'update_time': update_time,
    }

    return challenge


def format_return_param(code='001', message='', data=None):
    debug_log("format_return_param")
    if code == '002' or code == '003' or code == '004':
        error_logger.error(code, message)
    elif code =='900':
        system_error_logger.error(code, message)

    return {
        'result_cd': code,
        'message': message,
        'data': data
    }


def debug_log(log):
    # デバッグ用コンソール出力関数
    print(log, file=sys.stderr)