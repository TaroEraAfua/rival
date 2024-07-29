# coding: utf-8
import pymysql
from util.setting import Setting
import api.common.sql as format
import sys


class Chat(object):

    def __init__(self, challenge_id=None, log_no=None, send_team_id=None, user_name=None,
                 message=None, register_dt=None, update_time=None):
        self.challenge_id = challenge_id
        self.log_no = log_no
        self.send_team_id = send_team_id
        self.user_name = user_name
        self.message = message
        self.register_dt = register_dt
        self.update_time = update_time

    def to_dict(self):
        res = {
            "challenge_id": self.challenge_id,
            "log_no": self.log_no,
            "send_team_id": self.send_team_id,
            "send_user_id": self.user_name,
            "message": self.message,
            "register_dt": self.register_dt,
        }
        return res

    @classmethod
    def set_message(cls, message):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        print(message, file=sys.stderr)
        try:
            cur.execute(format.set_chat_log, message)
            conn.commit()
            print(cur._executed, file=sys.stderr)
        except Exception as e:
            print(e, file=sys.stderr)
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def get_message(cls, challenge_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(format.get_chat_log, {'challenge_id': challenge_id})
        result = cur.fetchall()
        cur.close()
        conn.close()

        chat_list = []
        for obj in result:
            chat_list.append(Chat(**obj))
        return result
