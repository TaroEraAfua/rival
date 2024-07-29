# coding: utf-8
import pymysql
from util.setting import Setting
import api.common.constant as constant
import api.common.sql as format
import datetime
import sys


class Team(object):

    def __init__(self, team_id=None, admin=None, sign_in_time=None, team_name=None, team_image=None,
                 prefecture_id=None, prefecture_name=None, city_id=None, city_name=None,
                 line_id=None, line_name=None, station_id=None, station_name=None,
                 gender=None, comment=None, week_id=None, time_id=None, join_status=None,
                 game_date=None, purpose_id=None, status=None, feature_id=None, feature_name=None,
                 challenge_id=None, send_team_id=None, res_team_id=None, count=None,
                 avg_age=None, solicitation_flg=None, gym=None, main_place=None, c_comment=None, u_comment=None,
                 member_num=None, stray_flg=None, game_time_start=None,game_time_end=None,
                 exec_type=None,game_status=None,challenge_status=None
                 ):

        self.count = count
        self.team_id = team_id
        self.admin = admin
        self.sign_in_time = sign_in_time
        self.avg_age = avg_age
        self.solicitation_flg = solicitation_flg
        self.gym = gym
        self.main_place = main_place
        self.team_name = team_name
        self.team_image = team_image
        self.prefecture_id = prefecture_id
        self.prefecture_name = prefecture_name
        self.city_id = city_id
        self.city_name = city_name
        self.line_id = line_id
        self.line_name = line_name
        self.station_id = station_id
        self.station_name = station_name
        self.gender = gender
        self.comment = comment
        self.week_id = week_id
        self.time_id = time_id
        self.game_date = game_date
        self.feature_id = feature_id
        self.feature_name = feature_name
        self.purpose_id = purpose_id
        self.challenge_id = challenge_id
        self.send_team_id = send_team_id
        self.status = status
        self.u_comment = u_comment
        self.c_comment = c_comment
        self.join_status = join_status
        self.member_num = member_num
        self.main_place = main_place
        self.stray_flg = stray_flg
        self.game_time_start = game_time_start
        self.game_time_end = game_time_end
        self.exec_type = exec_type
        self.game_status = game_status
        self.challenge_status = challenge_status

    def to_dict_count(self):
        res = {
            "count": self.count
        }
        return res

    def to_dict_team_info(self):

        res = {
            "team_id": self.team_id,
            "admin": self.admin,
            "team_name": self.team_name,
            "team_image": self.team_image,
            "prefecture_id": self.prefecture_id,
            "prefecture_name": self.prefecture_name,
            "city_id": self.city_id,
            "city_name": self.city_name,
            "line_id": self.line_id,
            "line_name": self.line_name,
            "station_id": self.station_id,
            "station_name": self.station_name,
            "gender": self.gender,
            "comment": self.comment,
            "feature_id": self.feature_id,
            "feature_name": self.feature_name,
            "main_place": self.main_place,
            "avg_age": self.avg_age,
            "gym": self.gym,
            "solicitation_flg": self.solicitation_flg,
            "purpose_id": self.purpose_id,
            "u_comment": self.u_comment,
            "c_comment": self.c_comment,
            "member_num": self.member_num,
            "challenge_id": self.challenge_id,
            "send_team_id": self.send_team_id,
            "status": self.status,
            "join_status": self.join_status,
            "stray_flg": self.stray_flg
        }
        return res

    def to_dict_week(self):
        res = {
            'team_id': self.team_id,
            'week_id': self.week_id,
            'time_id': self.time_id,
        }
        return res

    def to_dict_game_date(self):
        res = {
            "challenge_id": self.challenge_id,
            'team_id': self.team_id,
            'game_date': self.game_date,
            'game_time_start': self.game_time_start,
            'game_time_end': self.game_time_end,
            'exec_type': self.exec_type,
            'game_status': self.game_status,
            'comment': self.comment,
            "challenge_status": self.challenge_status
        }
        return res

    def to_dict_purpose(self):
        res = {
            'team_id': self.team_id,
            'purpose_id': self.purpose_id
        }
        return res

    def to_dict_feature(self):
        res = {
            'team_id': self.team_id,
            'feature_id': self.feature_id
        }
        return res

    def to_dict_come(self):
        res = {
            'team_name': self.team_name,
            'prefecture_name': self.prefecture_name,
            'city_name': self.city_name
        }
        return res

    @classmethod
    def get_team_list(cls, select_sql, from_sql, where_sql, offset=None, t_flg=True):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        group_by = '''
         group by prof.team_id
        , info.admin
        , prof.team_id
        , prof.team_name
        , prof.team_image
        , prof.prefecture_id
        , prof.city_id
        , city.city_name
        , prefecture.prefecture_name
        , prof.line_id
        , station.line_name
        , prof.station_id
        , station.station_name
        , prof.avg_age
        , prof.gym
        , prof.solicitation_flg
        , prof.stray_flg
        , prof.main_place
        , prof.member_num
        , prof.gender
        , prof.c_comment
        , prof.u_comment
        , j.status
        '''

        sql = ''
        sql += select_sql
        sql += from_sql
        sql += where_sql
        sql += group_by

        if type(offset) is int and t_flg:
            offset = 0
            c_sql = 'select count(team_id) as count from (select prof.team_id '
            c_sql += from_sql
            c_sql += where_sql
            c_sql += group_by
            c_sql += ' ) as cnt'
            cur.execute(c_sql)
            c_res = cur.fetchone()
            counter = c_res["count"]
        else:
            counter = None

        if t_flg:
            sql += ' LIMIT 20 OFFSET {}'.format(str(offset))
        cur.execute(sql)
        info = cur.fetchall()
        cur.close()
        conn.close()
        info_list = []
        for obj in info:
            info_list.append(Team(**obj))

        return info_list, counter

    @classmethod
    def get_team(cls, param):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        sql = format.get_team_profile()

        cur.execute(sql, param)
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result is None:
            return None
        else:
            return Team(**result)

    @classmethod
    def set_team(cls, user_id, info, prof, purpose, feature):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)

        try:
            cur.execute(format.check_user, {"user_id": user_id})
            result = cur.fetchone()
            if result['owner_num'] <= result['count']:
                return {'message': 'これ以上チーム登録はできません'}

            cur.execute(format.set_team_info, info)
            # cur.executemany(format.set_t_week, week)
            cur.execute(format.set_team_prof, prof)
            cur.executemany(format.set_t_purpose, purpose)
            cur.executemany(format.set_t_feature, feature)

            conn.commit()
        except Exception as e:
            print(e, file=sys.stderr)
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def update_team_profile(cls, team_id, prof, purpose, feature, game_date):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        # d_week = 'DELETE FROM t_week WHERE team_id = %s'
        d_purpose = 'DELETE FROM t_purpose WHERE team_id = %s'
        d_game_date = 'DELETE FROM t_game_date WHERE team_id = %s where challenge_id != "" '
        d_feature = 'DELETE FROM t_feature WHERE team_id = %s'
        try:
            # cur.execute(d_week, team_id)
            cur.execute(d_purpose, team_id)
            cur.execute(d_game_date, team_id)
            cur.execute(d_feature, team_id)

            cur.execute(format.set_team_prof, prof)
            # cur.executemany(format.set_t_week, week)
            cur.executemany(format.set_t_purpose, purpose)
            cur.executemany(format.set_t_feature, feature)

            if game_date is not None:
                cur.executemany(format.set_t_game_date, game_date)

            conn.commit()
        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def update_team_info(cls, info):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.set_team_info, info)
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def delete_team_info(cls, team_id, user_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        sql = 'DELETE FROM team_info WHERE team_id = %s and user_id = %s'
        try:
            cur.execute(sql, [team_id, user_id])
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def update_team_game_date(cls, team_id, game_date):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        d_game_date = 'DELETE FROM t_game_date WHERE team_id = %s'
        s_game_date = 'SELECT game_date, game_time_start, game_time_end as cnt FROM t_game_date WHERE team_id = %s AND game_status = 1'
        try:
            cur.execute(s_game_date, team_id)
            info = cur.fetchall()
            cnt = 0
            print('update_team_game_date', file=sys.stderr)
            print(info, file=sys.stderr)
            print(game_date, file=sys.stderr)
            for oldG in info:
                print(oldG['game_time_start'], file=sys.stderr)
                for newG in game_date:
                    if oldG['game_date'].strftime("%Y/%m/%d") == newG['game_date'] \
                            and str(oldG['game_time_start']) == newG['game_time_start']:
                        tmpDate.append(oldG['game_time_start'])
                        tmpStart.append(oldG['game_date'])
                        cnt += 1

            if len(info) == cnt:
                if len(tmpDate) > 0:
                    d_game_date += ' ( "' + '","'.join(tmpDate) + '" ) '
                    d_game_date += ' ( "' + '","'.join(tmpStart) + '" ) '
                cur.execute(d_game_date, team_id)
                cur.executemany(format.set_t_game_date, game_date)
                conn.commit()
            else:
                conn.commit()
                return {'message': constant.MESSAGE_ERR_006}

        except Exception as e:
            conn.rollback()
            print(e, file=sys.stderr)
            if 'Duplicate' in str(e):
                return {'message': constant.MESSAGE_ERR_007}
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def check_info(cls, team_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)

        sql = 'select team_id from team_info where team_id = %s'
        cur.execute(sql, team_id)
        result = cur.fetchone()
        cur.close()
        conn.close()
        if result:
            return Team(**result)
        else:
            return None

    @classmethod
    def add_team_user(cls, send):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            cur.execute(format.add_team_user, send)
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        return

    @classmethod
    def get_all_team(cls):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        sql = '''
            SELECT 
             tp.team_name
             , pm.prefecture_name
             , cm.city_name
            FROM team_profile as tp
            INNER JOIN
                prefectures_master as pm
            ON 
                pm.prefecture_id = tp.prefecture_id
            LEFT JOIN
                city_master as cm
            ON 
                cm.prefecture_id = tp.prefecture_id
            AND
                cm.city_id = tp.city_id
        '''

        cur.execute(sql)
        info = cur.fetchall()
        cur.close()
        conn.close()

        info_list = []
        for obj in info:
            info_list.append(Team(**obj).to_dict_come())

        return info_list

    @classmethod
    def get_count(cls):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        cnt_sql = 'select const_sub_name as count from const_master where const_id = 9999'
        t_cnt_sql = 'select count(team_id) as count from team_profile group by team_id'
        try:
            cur.execute(cnt_sql)
            cnt = cur.fetchone()
            cur.execute(t_cnt_sql)
            t_cnt = cur.fetchone()
            conn.commit()
        except Exception as e:
            conn.rollback()

            return 0
        finally:
            cur.close()
            conn.close()

        res = int(cnt['count'])
        if t_cnt:
            res += int(t_cnt['count'])

        return res

    @classmethod
    def get_game_date(cls, team_id, w_sql, search_flg):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)

        try:
            sql = format.get_t_game_date
            if search_flg:
                sql += ' where ' + w_sql
            else:
                sql += ''' 
                         where A.team_id = %(team_id)s or c.send_team_id = %(team_id)s  
                       '''
            cur.execute(sql, {"team_id": team_id})
            #
            print(cur._executed, file=sys.stderr)
            info = cur.fetchall()

        except Exception as e:
            print(e, file=sys.stderr)
            conn.rollback()
            return False

        finally:
            cur.close()
            conn.close()

        info_list = []
        for obj in info:
            info_list.append(Team(**obj))
        return info_list

    @classmethod
    def get_feature(cls, w_sql):
        print(w_sql, file=sys.stderr)
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            sql = format.get_t_feature
            sql += ' where '
            sql += w_sql
            cur.execute(sql)
            info = cur.fetchall()
        except Exception as e:
            print(e, file=sys.stderr)
            conn.rollback()
            return False
        finally:
            cur.close()
            conn.close()

        info_list = []
        for obj in info:
            info_list.append(Team(**obj))
        return info_list

    @classmethod
    def get_purpose(cls, w_sql):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)

        try:
            sql = format.get_t_purpose
            sql += ' where '
            sql += w_sql
            cur.execute(sql)
            info = cur.fetchall()

        except Exception as e:
            conn.rollback()
            return False

        finally:
            cur.close()
            conn.close()

        info_list = []
        for obj in info:
            info_list.append(Team(**obj))
        return info_list

    @classmethod
    def get_week(cls, w_sql):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            sql = format.get_t_week
            sql += ' where '
            sql += w_sql
            cur.execute(sql)
            info = cur.fetchall()

        except Exception as e:
            conn.rollback()
            return False

        finally:
            cur.close()
            conn.close()

        info_list = []
        for obj in info:
            info_list.append(Team(**obj))
        return info_list

    @classmethod
    def delete_team_account(cls, team_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        t_challenge = 'delete from t_challenge where team_id = %s'
        t_feature = 'delete from t_feature where team_id = %s'
        t_game_date = 'delete from t_game_date where team_id = %s'
        t_level = 'delete from t_level where team_id = %s'
        t_purpose = 'delete from t_purpose where team_id = %s'
        t_week = 'delete from t_week where team_id = %s'
        team_profile = 'delete from team_profile where team_id = %s'
        team_info = 'delete from team_info where team_id = %s'

        try:
            cur.execute(t_challenge, team_id)
            cur.execute(t_feature, team_id)
            cur.execute(t_game_date, team_id)
            cur.execute(t_level, team_id)
            cur.execute(t_purpose, team_id)
            cur.execute(t_week, team_id)
            cur.execute(team_profile, team_id)
            cur.execute(team_info, team_id)
            conn.commit()

        except Exception as e:
            conn.rollback()
            return {'message': e}
        finally:
            cur.close()
            conn.close()

    @classmethod
    def get_team_name(cls, w_sql):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        try:
            sql = 'SELECT team_id, team_name FROM team_profile WHERE ' + w_sql
            cur.execute(sql)

            info = cur.fetchall()
        except Exception as e:
            return {'message': e}
        finally:
            cur.close()
            conn.close()

        res = {}
        for row in info:
            res[row['team_id']] = row['team_name']
        return res
