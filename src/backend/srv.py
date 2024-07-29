#!/usr/bin/python3
# coding: utf-8
import io
import sys
import codecs
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from flask import Flask, jsonify, request, redirect, url_for, Response, make_response, abort

import api.controller.chat as chat
import api.controller.team as team
import api.controller.user as user
import api.controller.const as const
import api.controller.challenge as challenge
import argparse
from api.common.unit import debug_log
from flask_cors import CORS
from util.setting import Setting
import util.crypt as AESCipher
app = Flask(__name__)
CORS(app)

devEnv = False


def check_param(request, auth=False):
    debug_log("check_param")
    token = request.headers.get("token")
    body = request.json
    req = body

    if "param" in body:
        # 復号
        if devEnv:
            req = body["param"]
        else:
            if body["param"] is not None:
                req = AESCipher.decrypt(body["param"], token)
                req = json.loads(req.encode('utf_8'))
            else:
                req = body["param"]
    return req


def return_param(result, request):
    debug_log("return_param")
    # ステータスコードを設定する
    # 戻ってきたものに値があれば判定,Noneであれば200(検索0件時、データ更新時)
    token = request.headers.get("token")
    res = Response()
    if result is not None:
        if 'err' in result.keys():
            res.status_code = 400
        else:
            res.status_code = 200

        # response暗号化
        data = None
        if devEnv:
            res = jsonify(result_cd=result["result_cd"], message=result["message"], data=result["data"])
        else:
            if result["data"] is not None:
                data = AESCipher.encrypt(json.dumps(result["data"]), token)
            res = jsonify(result_cd=result["result_cd"], message=result["message"], data=data)

    else:
        # dataがNoneの場合statusに200を設定する
        res.status_code = 500
        res.message = 'システムエラー'
        res.result_code = 900
    res.headers['Content-Type'] = 'application/json;charset=UTF-8'
    res.headers['Access-Control-Allow-Origin'] = '*'
    res.headers['Access-Control-Allow-Methods'] = '*'
    res.headers['Access-Control-Allow-Headers'] = '*'
    return res


@app.route('/api/health', methods=['POST'])
def health():
    return "OK"


@app.route('/api/const/get_const_data', methods=['POST'])
def get_const_data():
    # 定数取得
    res = const.get_const_data()

    return return_param(res, request)


@app.route('/api/area/get_prefecture', methods=['POST'])
def get_prefecture():
    req = check_param(request)
    # 都道府県の定数データを取得
    res = const.get_prefecture()

    return return_param(res, request)


@app.route('/api/area/get_city', methods=['POST'])
def get_city():
    # 市区町村の定数データを取得
    req = check_param(request)
    prefecture_id = req['id']
    res = const.get_city(prefecture_id)

    return return_param(res, request)


@app.route('/api/area/get_station', methods=['POST'])
def get_station():
    # 駅の定数データを取得
    req = check_param(request)
    prefecture_id = req['prefecture_id']
    city_name = req['city_name']

    res = const.get_station(prefecture_id, city_name)

    return return_param(res, request)


@app.route('/api/team/search_detail', methods=['POST'])
def search_detail():
    # 詳細検索
    req = check_param(request)
    user_id = req['user']
    team_id = req['team']
    # user_id = None
    prefecture_id = req['prefecture']
    city_id = req['city']
    station = req['station']
    if station:
        station_id = station['station_id']
        line_id = station['line_id']
    else:
        station_id = ''
        line_id = ''

    gender = req['gender']
    purpose_list = req['purpose']
    week_list = None
    offset = req['page']
    res = team.get_from_detail(team_id, user_id, prefecture_id, city_id, station_id,
                               line_id, gender, purpose_list, week_list, offset)

    return return_param(res, request)


@app.route('/api/team/search_date', methods=['POST'])
def search_date():
    # 日付検索
    req = check_param(request)
    user_id = req['user']
    team_id = req['team']
    prefecture_id = req['prefecture']
    station = req['station']
    city = req['city']
    if station:
        station_id = station['station_id']
        line_id = station['line_id']
    else:
        station_id = ''
        line_id = ''

    date_list = req['date']
    offset = req['page']
    res = team.get_from_game_date(team_id, user_id, date_list, prefecture_id, city, station_id, line_id, offset)
    return return_param(res, request)


@app.route('/api/team/add_account', methods=['POST'])
def add_team():
    # チーム追加
    req = check_param(request)
    team_id = req['team_id']
    team_name = req['team_name']
    user_id = req['user_id']
    admin = req['admin']
    icon_json = req['image']
    if icon_json is not None and ('image_name' in icon_json and 'image_data' in icon_json):
        image_name = icon_json['image_name']
        image_data = icon_json['image_data']
    else:
        image_name = ''
        image_data = ''
    prefecture = req['prefecture']
    city = req['city']
    station = req['station']
    gender = req['gender']
    purpose = req['purpose']
    game_date = req['game_date']
    gym = req['gym']
    stray_flg = req['stray_flg']
    feature = req['feature']
    average_age = req['average_age']
    main_place = req['main_place']
    member_num = req['member_num']
    solicitation = req['solicitation']
    c_comment = req['c_comment']
    u_comment = req['u_comment']
    res = team.add_account(team_id, user_id, admin, team_name, image_data, image_name, prefecture, city,
                           station, gender, purpose, game_date, gym, main_place, feature, average_age,
                           member_num, stray_flg, solicitation, c_comment, u_comment)
    return return_param(res, request)


@app.route('/api/team/update_team_info', methods=['POST'])
def update_team_info():
    # チームデータ更新
    req = check_param(request)
    team_id = req['team_id']
    user_id = req['user_id']
    admin = req['admin']
    res = team.update_team_info(team_id, user_id, admin)
    return return_param(res, request)


@app.route('/api/team/update_team_profile', methods=['POST'])
def update_team_profile():
    # チーム情報を更新する
    req = check_param(request)
    team_id = req['team_id']
    user_id = req['user_id']
    team_name = req['team_name']
    icon_json = req['image']
    if icon_json is not None and ('image_name' in icon_json and 'image_data' in icon_json):
        image_name = icon_json['image_name']
        image_data = icon_json['image_data']
    else:
        image_name = ''
        image_data = ''
    prefecture = req['prefecture']
    city = req['city']
    station = req['station']
    gender = req['gender']
    game_date = req['game_date']
    gym = req['gym']
    average_age = req['average_age']
    feature = req['feature']
    purpose = req['purpose']
    week = None
    main_place = req['main_place']
    member_num = req['member_num']
    stray_flg = req['stray_flg']
    solicitation = req['solicitation']
    c_comment = req['c_comment']
    u_comment = req['u_comment']
    admin = 1
    res = team.update_team_profile(team_id, user_id, admin, team_name, image_data, image_name, prefecture, city,
                                   station, gender, purpose, game_date, gym, main_place, feature, average_age,
                                   member_num, stray_flg, solicitation, c_comment, u_comment)

    return return_param(res, request)


@app.route('/api/team/update_team_game_date', methods=['POST'])
def update_team_game_date():
    # チームの実施日付を更新する
    req = check_param(request)
    team_id = req['team_id']
    game_date = req['game_date']
    res = team.update_team_game_date(team_id, game_date)
    return return_param(res, request)


@app.route('/api/team/delete_team_user', methods=['POST'])
def delete_team_user():
    # チーム情報を削除
    req = check_param(request)
    team_id = req['team_id']
    user_id = req['user_id']
    res = team.delete_team_info(team_id, user_id)
    return return_param(res, request)


@app.route('/api/team/check_team_id', methods=['POST'])
def check_team_id():
    # チーム有無確認 エラーなし
    req = check_param(request)
    team_id = req['team_id']

    res = team.check_team_id(team_id)
    return return_param(res, request)


@app.route('/api/team/add_team_user', methods=['POST'])
def add_team_user():
    # チームを追加する
    req = check_param(request)
    team_id = req['team_id']
    user_id = req['user_id']
    message = req['message']
    status = req['status']
    res = team.add_team_user(team_id, user_id, message, status)
    return return_param(res, request)


@app.route('/api/chat/get_chat_log', methods=['POST'])
def get_chat_log():
    # チャット取得
    req = check_param(request)
    challenge_id = req['challenge_id']
    res = chat.get_chat_log(challenge_id)
    return return_param(res, request)


@app.route('/api/chat/set_chat_log', methods=['POST'])
def set_chat_log():
    # チャット処理
    req = check_param(request)
    challenge_id = req['challenge_id']
    team_id = req['team_id']
    user_id = req['user_id']
    # log_no = req['log_no']
    message = req['message']

    res = chat.set_chat_log(challenge_id, team_id, user_id, message)
    return return_param(res, request)


@app.route('/api/user/get_user', methods=['POST'])
def get_user():
    # ユーザIDに紐づく情報を取得
    req = check_param(request)
    user_id = req['user_id']
    res = user.get_user(user_id)
    return return_param(res, request)


@app.route('/api/user/check_user', methods=['POST'])
def check_user():
    # ユーザーの存在確認を行う
    req = check_param(request)
    user_id = req['user_id']
    res = user.check_user(user_id)

    return return_param(res, request)


@app.route('/api/user/sign_in', methods=['POST'])
def sign_in():
    # ユーザ認証を行う
    req = check_param(request)
    user_id = req['user_id']
    password = req['password']
    res = user.sign_in(user_id, password)

    return return_param(res, request)


@app.route('/api/user/update_pass', methods=['POST'])
def update_pass():
    # ユーザパスワードを更新する
    req = check_param(request)
    user_id = req['user_id']
    password_old = req['password_old']
    password_new = req['password_new']
    res = user.update_pass(user_id, password_old, password_new)

    return return_param(res, request)


@app.route('/api/user/set_user', methods=['POST'])
def set_user():
    # ユーザー情報を設定する
    req = check_param(request)
    user_id = req['user_id']
    user_name = req['user_name']
    mail = req['mail']
    password = req['password']
    prefecture = req['prefecture']
    city = req['city']
    birth_dt = req['birth_dt']
    gender = req['gender']
    week = None

    # 暫定対応
    icon_json = req['user_icon']
    if icon_json is not None and ('image_name' in icon_json and 'image_data' in icon_json):
        image_name = icon_json['image_name']
        image_data = icon_json['image_data']
    else:
        image_name = ''
        image_data = ''
    position = req['position']
    height = req['height']
    ex_year = req['ex_year']
    ex_width = req['ex_width']
    message = req['message']

    res = user.add_user(user_id, user_name, password, prefecture, city,
                        gender, birth_dt, mail, image_name, image_data, height, position, ex_year, ex_width, message)
    return return_param(res, request)


@app.route('/api/user/update_user', methods=['POST'])
def update_user():
    # ユーザー情報を更新する
    req = check_param(request)
    user_id = req['user_id']
    user_name = req['user_name']
    mail = req['mail']
    prefecture = req['prefecture']
    city = req['city']
    birth_dt = req['birth_dt']
    gender = req['gender']


    # 暫定対応
    icon_json = req['user_icon']
    if icon_json is not None and ('image_name' in icon_json and 'image_data' in icon_json):
        image_name = icon_json['image_name']
        image_data = icon_json['image_data']
    else:
        image_name = ''
        image_data = ''
    position = req['position']
    height = req['height']
    ex_year = req['ex_year']
    ex_width = req['ex_width']
    message = req['message']

    res = user.update_user(user_id, user_name, prefecture, city, gender,
                           birth_dt, mail, image_name, image_data, height, position, ex_year, ex_width, message)

    return return_param(res, request)


@app.route('/api/challenge/get_team', methods=['POST'])
def get_team():
    # challenge情報設定
    req = check_param(request)
    team_id = req['team_id']
    res = challenge.get_team(team_id)

    return return_param(res, request)


@app.route('/api/team/get_team_profile', methods=['POST'])
def get_team_profile():
    # challenge情報設定
    req = check_param(request)
    team_id = req['team_id']
    user_id = req['user_id']
    res = team.get_team_profile(team_id, user_id)

    return return_param(res, request)


@app.route('/api/challenge/set_challenge', methods=['POST'])
def set_challenge():
    # challenge情報設定
    req = check_param(request)
    send_id = req['target_id']
    res_id = req['team_id']
    game_date = req['game_date']
    game_time_start = req['game_time_start']

    res = challenge.set_challenge(send_id, res_id, game_date, game_time_start)

    return return_param(res, request)


@app.route('/api/challenge/delete_challenge', methods=['POST'])
def delete_challenge():
    # challenge情報削除
    req = check_param(request)
    challenge_id = req['challenge_id']
    res = challenge.delete_challenge(challenge_id)

    return return_param(res, request)


@app.route('/api/challenge/get_challenge', methods=['POST'])
def get_challenge():
    # challenge情報取得
    req = check_param(request)
    team_id = req['team_id']
    res = challenge.get_challenge(team_id)

    return return_param(res, request)


@app.route('/api/challenge/set_match', methods=['POST'])
def set_match():
    # challenge情報取得
    req = check_param(request)
    challenge_id = req['challenge_id']
    status = 1
    res = challenge.change_challenge_status(challenge_id, status)

    return return_param(res, request)


@app.route('/api/team/get_all', methods=['POST'])
def get_all_team():
    # 登録件数を取得する  エクセプション時でも０件を返却する
    res = team.get_count()
    return return_param(res, request)


@app.route('/api/team/join_team', methods=['POST'])
def join_team():
    # チームデータ更新
    req = check_param(request)
    team_id = req['team_id']
    user_id = req['user_id']
    res = team.add_team_user(team_id, user_id)
    return return_param(res, request)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', '-d', action='store_const', const=True, default=False)
    args = parser.parse_args()
    if args.dev:
        devEnv = True
        app.run(host='0.0.0.0', debug=True, port=2000)
    else:
        app.run(host='0.0.0.0', debug=True, threaded=True)
