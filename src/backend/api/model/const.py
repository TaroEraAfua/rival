
# coding: utf-8
import pymysql
from util.setting import Setting


class Const(object):

    def __init__(self, const_name=None, const_sub_id=None, const_sub_name=None):
        self.const_name = const_name
        self.const_sub_id = const_sub_id
        self.const_sub_name = const_sub_name

    def to_dict(self):
        res = {
            'const_name': self.const_name,
            'const_sub_id': self.const_sub_id,
            'const_sub_name': self.const_sub_name,
        }
        return res

    @classmethod
    def get_const(cls):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)

        sql = 'select const_name, const_sub_id, const_sub_name from const_master order by const_name'

        cur.execute(sql)
        const = cur.fetchall()
        cur.close()
        conn.close()
        const_list = []
        for obj in const:
            const_list.append(Const(**obj))

        return const_list

    @classmethod
    def get_icon(cls, icon_id):
        conn = pymysql.connect(**Setting().db_init)
        cur = conn.cursor(pymysql.cursors.DictCursor)

        sql = '''
            select 
                const_name, 
                const_sub_id, 
                const_sub_name 
            from const_master 
            where 
                const_id = "{}" 
                and const_sub_id = "{}"
            '''.format(10, icon_id)

        cur.execute(sql)
        const = cur.fetchall()
        cur.close()
        conn.close()
        const_list = []
        for obj in const:
            const_list.append(Const(**obj))

        return const_list

