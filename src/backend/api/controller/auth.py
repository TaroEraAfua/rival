# coding: utf-8
from ..model.user import User
from api.common.unit import debug_log


def get_user(token, user_id=None):

    try:
        debug_log("作成中")
    except Exception as e:
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response