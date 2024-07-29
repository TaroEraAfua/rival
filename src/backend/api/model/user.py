# coding: utf-8
import pymysql
from util.setting import Setting
import api.common.sql as format
import sys
import api.common.constant as constant


class User(object):

    def __init__(self, user_id=None, user_name=None, password=None, prefecture_id=None, prefecture_name=None,
                 line_id=None, line_name=None, station_id=None, station_name=None,
                 city_id=None, city_name=None, birth_dt=None, gender=None, icon=None,
                 week_id=None, time_id=None, position_id=None, width_id=None, ex_year=None, height=None, comment=None):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.icon = icon
        self.prefecture_id = prefecture_id
        self.prefecture_name = prefecture_name
        self.city_id = city_id
        self.city_name = city_name
        self.line_id = line_id
        self.line_name = line_name
        self.station_id = station_id
        self.station_name = station_name
        self.birth_dt = birth_dt
        self.gender = gender
        self.week_id = week_id
        self.time_id = time_id
        self.width_id = width_id
        self.height = height
        self.comment = comment
        self.ex_year = ex_year
        self.position_id = position_id

    def to_dict(self):
        res = {
            'user_id': self.user_id,
            'user_name': self.user_name,
            'password': self.password,
            'prefecture_id': self.prefecture_id,
            'prefecture_name': self.prefecture_name,
            'city_id': self.city_id,
            'city_name': self.city_name,
            "line_id": self.line_id,
            "line_name": self.line_name,
            "station_id": self.station_id,
            "station_name": self.station_name,
            'birth_dt': self.birth_dt,
            'icon': self.icon,
            'gender': self.gender,
            "week_id": self.week_id,
            "time_id": self.time_id,
            "width_id": self.width_id,
            "height": self.height,
            "message": self.comment,
            "ex_year": self.ex_year,
            "position_id": self.position_id,
        }
        return res

    def to_dict_sign(self):
        res = {
            'user_id': self.user_id,
        }
        return res

    @classmethod
    def check_user(cls, user_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.check_user_id, {'user_id': user_id})
            conn.commit()
            c_res = cur.fetchone()
            # ０件でもエラーにしない対応
            if c_res is not None:
                response = User(**c_res)
            else:
                response = c_res
        except Exception as e:
            conn.rollback()
            return
        finally:
            cur.close()
            conn.close()

        return response

    @classmethod
    def get_user_prof(cls, user_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.get_user_prof, {'user_id': user_id})
            result = cur.fetchall()
        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()
        prof = []
        for obj in result:
            prof.append(User(**obj))
        return prof

    @classmethod
    def get_user_position(cls, user_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.get_u_position, {'user_id': user_id})
            result = cur.fetchall()
        except Exception as e:
            conn.rollback()
            return False
        finally:
            cur.close()
            conn.close()
        prof = []
        for obj in result:
            prof.append(User(**obj))
        return prof

    @classmethod
    def set_user_info(cls, user_id, user, ex_width, position):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        # d_week = 'DELETE FROM u_week WHERE user_id = %s'
        d_position = 'DELETE FROM u_position WHERE user_id = %s'
        d_ex_width = 'DELETE FROM u_ex_width WHERE user_id = %s'

        try:
            # cur.execute(d_week, user_id)
            cur.execute(d_position, user_id)
            cur.execute(d_ex_width, user_id)
            cur.execute(format.set_user_info, user)
            # cur.executemany(format.set_u_week, week)
            cur.executemany(format.set_u_ex, ex_width)
            cur.executemany(format.set_u_position, position)
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def sign_in(cls, user):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.update_user_sign_in, user)
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return True

    @classmethod
    def update_user_pass(cls, user):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.update_user_pass, user)
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def check_favorite_team(cls, user):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.check_favorite_team, user)
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def delete_user_account(cls, user_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        u_ex_width = 'delete from u_ex_width where user_id = %s'
        u_favorite = 'delete from u_favorite where user_id = %s'
        u_position = 'delete from u_position where user_id = %s'
        u_week = 'delete from u_week where user_id = %s'
        user_info = 'delete from user_info where user_id = %s'
        try:
            cur.execute(u_ex_width, user_id)
            cur.execute(u_favorite, user_id)
            cur.execute(u_position, user_id)
            cur.execute(u_week, user_id)
            cur.execute(user_info, user_id)
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()
