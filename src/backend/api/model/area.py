# coding: utf-8
import pymysql
from util.setting import Setting


class Area(object):

    def __init__(self, prefecture_id=None, prefecture_name=None, city_id=None,
                 city_name=None, city_level=None, line_id=None, line_name=None,
                 station_id=None, station_name=None, address=None):

        self.prefecture_id = prefecture_id
        if prefecture_name is not None:
            self.prefecture_name = prefecture_name
        if city_id is not None:
            self.city_id = city_id
            self.city_name = city_name
            self.city_level = city_level
        if line_id is not None or station_id is not None:
            self.line_id = line_id
            self.line_name = line_name
            self.station_id = station_id
            self.station_name = station_name
            self.address = address

    def to_dict_prefecture(self):
        res = {
            "prefecture_id": self.prefecture_id,
            "prefecture_name": self.prefecture_name,
        }
        return res

    def to_dict_city(self):
        res = {
            "city_id": self.city_id,
            "city_name": self.city_name,
            "city_level": self.city_level,
        }
        return res

    def to_dict_station(self):
        res = {
            "line_id": self.line_id,
            "line_name": self.line_name,
            "station_id": self.station_id,
            "station_name": self.station_name,
        }
        return res

    @classmethod
    def get_prefecture(cls):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        sql = '''
                select 
                 prefecture_id,
                 prefecture_name
                from prefectures_master
            '''
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        conn.close()
        prefectures = []
        for obj in res:
            prefectures.append(Area(**obj).to_dict_prefecture())
        return prefectures

    @classmethod
    def get_city(cls, prefecture_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        sql = '''
                select 
                 city_id,
                 city_name
                from 
                 city_master
                where
                 prefecture_id = %s
            '''
        cur.execute(sql, prefecture_id)
        res = cur.fetchall()
        cur.close()
        conn.close()
        city = []
        for obj in res:
            city.append(Area(**obj).to_dict_city())
        return city

    @classmethod
    def get_station(cls, prefecture_id, city_name):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)
        sql = '''
                select 
                 line_id,
                 line_name,
                 station_id,
                 station_name
                from 
                 station_master
                where
                 prefecture_id = %(prefecture)s
                and
                 address like %(address)s
            '''
        cur.execute(sql, {'prefecture': prefecture_id, 'address': '%' + city_name + '%'})
        res = cur.fetchall()
        cur.close()
        conn.close()
        station = []
        for obj in res:
            station.append(Area(**obj).to_dict_station())
        return station
