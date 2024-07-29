# coding: utf-8
import os
import sys


class Setting(object):
    def __init__(self):
        print(os.uname()[1], file=sys.stderr)
        if os.uname()[1] == 'rival01':
            self.db_init = {
                'host': 'localhost',
                'user': 'rival',
                'password': '8xyM_7vbhn4s',
                'db': 'rival',
                'charset': 'utf8',
            }
        else:
            self.db_init = {
                'host': 'rival2',
                'user': 'root',
                'password': 'root',
                'db': 'rival',
                'charset': 'utf8',
                'port': 3306
            }
