# coding: utf-8
import pymysql
from util.setting import Setting
import api.common.sql as format


class Challenge(object):

    def __init__(self, challenge_id=None, team_id=None,
                 challenge_status=None, game_time_start=None,
                 game_time_end=None, register_dt=None, update_time=None,
                 exec_type=None, game_status=None, game_date=None, comment=None,
                 send_team_id=None
                 ):
        self.challenge_id = challenge_id
        self.team_id = team_id
        self.send_team_id = send_team_id
        self.challenge_status = challenge_status
        self.game_date = game_date
        self.game_status = game_status
        self.game_time_start = game_time_start
        self.game_time_end = game_time_end
        self.exec_type = exec_type
        self.comment = comment
        self.register_dt = register_dt
        self.update_time = update_time

    def to_dict(self):
        res = {
            "challenge_id": self.challenge_id,
            "send_team_id": self.send_team_id,
            "team_id": self.team_id,
            "game_date": self.game_date,
            "game_time_start": self.game_time_start,
            "game_time_end": self.game_time_end,
            "challenge_status": self.challenge_status,
            "exec_type": self.exec_type,
            "game_status": self.game_status,
            "comment": self.comment
        }
        return res

    @classmethod
    def get_challenge_state(cls, team_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cur.execute(format.get_challenge, {"team_id": team_id})
        challenge = cur.fetchall()
        cur.close()
        conn.close()
        challenge_list = []
        for obj in challenge:
            challenge_list.append(Challenge(**obj))
        return challenge_list

    @classmethod
    def set_challenge(cls, params):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.set_t_challenge, params)
            conn.commit()
        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def update_challenge(cls, params):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.update_t_challenge, params)
            conn.commit()
        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def del_challenge(cls, challenge_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        sql = ' DELETE FROM t_challenge WHERE challenge_id = %s '
        try:
            cur.execute(sql, challenge_id)
            conn.commit()
        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return
