# coding: utf-8
import requests
import json
import pymysql.cursors
import pandas as pd
import datetime

def main():
    conn = con_mysql()
    id_list = get_prefectures(conn)
    set_city(conn, id_list)


def con_mysql():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='rival',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def get_prefectures(conn):

    with conn.cursor() as cursor:
        sql = 'SELECT prefecture_id, prefecture_name FROM prefectures_master where prefecture_id != %s'
        cursor.execute(sql, ('00',))
        result = cursor.fetchall()

    return result


def set_city(conn, id_list):
    url = 'http://www.land.mlit.go.jp/webland/api/CitySearch?area='
    to_day = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    sub_sql = '''
                insert into city_master 
                    (prefecture_id, city_id, city_name, city_level, update_time) 
                VALUES (%s, %s, %s, %s, %s)
           '''

    cnt = 1
    for row in id_list:
        res = requests.get(url + row['prefecture_id'])
        lists = json.loads(res.text)
        sub_area = []
        for sub in lists['data']:
            sub_area.append([row['prefecture_id'], sub['id'], sub['name'], float(0), to_day])
            cnt += 1
        cur = conn.cursor()
        cur.executemany(sub_sql, sub_area)
        conn.commit()


if __name__ == '__main__':
    main()