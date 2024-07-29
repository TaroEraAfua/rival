# coding: utf-8
import datetime
from api.model.chat import Chat
from api.common.unit import debug_log
import api.common.constant as constant
import api.common.unit as format


def get_chat_log(challenge_id):
    debug_log('get_chat_log')
    try:
        result = Chat.get_message(challenge_id)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            result
        )
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response


def set_chat_log(challenge_id, team_id, user_id, message):
    response = {}
    try:
        to_day = datetime.datetime.today()
        chat = {
            'challenge_id': challenge_id,
            'send_user_id': user_id,
            'send_team_id': team_id,
            'message': message,
            'register_dt': to_day.strftime("%Y-%m-%d"),
            'update_time': to_day.strftime("%Y-%m-%d %H:%M:%S")
        }
        Chat.set_message(chat)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001
        )
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response
