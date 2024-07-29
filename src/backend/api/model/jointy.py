# coding: utf-8
import pymysql
from util.setting import Setting


class Jointy(object):

    def __init__(self, prefecture_id=None, prefecture_name=None, city_id=None,
                 city_name=None, city_level=None, line_id=None, line_name=None,
                 station_id=None, station_name=None, address=None):