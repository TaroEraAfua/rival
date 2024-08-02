# coding: utf-8
from ..model.user import User
from api.common.unit import debug_log
from ..util.crypt import encrypt, decrypt
from ..util import format
from .. import constant

def get_user(token, user_id=None):

    try:
        user = User.check_user(user_id)
        if user:
            encrypted_password = encrypt(user.password, token)
            user.password = encrypted_password
            debug_log("User found: {}".format(user.to_dict()))
            response = user.to_dict()
        else:
            debug_log("User not found")
            response = format.format_return_param(
                constant.RESULT_CODE_ERR_SYSTEM,
                constant.MESSAGE_ERR_SYSTEM
            )
    except Exception as e:
        debug_log(e)
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )
    return response