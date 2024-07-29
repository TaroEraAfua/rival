import requests
import json
import pymysql.cursors
import pandas as pd
import datetime

def main():
    conn = con_mysql()
    id_list = get_main_area(conn)
    set_sub_area(conn, id_list)


def con_mysql():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='rival',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def get_main_area(conn):

    with conn.cursor() as cursor:
        sql = 'SELECT id, name FROM area where id != %s'
        cursor.execute(sql, ('00',))
        result = cursor.fetchall()

    return result


def set_sub_area(conn, id_list):
    url = 'http://geoapi.heartrails.com/api/json?method=getCities&prefecture='
    to_day = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    sql = '''
                insert into sub_area 
                    (area_id, sub_area_id, name, area_level, update_time) 
                VALUES (%s, %s, %s, %s, %s)
           '''
    df = pd.read_csv('x-ken-all.csv', encoding='sjis', usecols=[2, 6, 7, 8], header=None)
    df.columns = ['zip_code', 'l_area', 'm_area', 's_area']
    cnt = 1
    zip_list = []
    for row in id_list:
        res = requests.get(url + row['name'])
        lists = json.loads(res.text)
        sub_area = []
        for sub in lists['response']['location']:
            sub_area.append([row['id'], str(cnt), sub['city'], float(0), to_day])
            for idx, z_row in df[df['m_area'] == sub['city']].iterrows():
                zip_list.append([str(cnt), str(z_row['zip_code'])])
            cnt += 1

        cur = conn.cursor()
        cur.executemany(sql, sub_area)
        conn.commit()

    df = pd.DataFrame(zip_list, columns=['sub_area_id', 'zip_code'])
    df = df.drop_duplicates()
    set_station(conn, df)


def set_station(conn, zip_list):
    url = 'http://geoapi.heartrails.com/api/json?method=getStations&postal='
    line_id = 0
    t_line = {}
    station_list = []
    sql = '''
            insert into station (sub_are_id, lind_id, line_name, station_id, station_name)
            values (%s, %s, %s, %s, %s)
          '''
    station_id = 0
    for idx, z_row in zip_list.iterrows():
        res = requests.get(url + z_row['zip_code'])
        lists = json.loads(res.text)

        if 'station' in lists['response'].keys():
            for row in lists['response']['station']:
                if row['line'] in t_line.keys():
                    if not row['name'] in t_line[row['line']]['station'].keys():
                        station_list.append([z_row['sub_area_id'], t_line[row['line']]['id'], row['line'], station_id, row['name']])
                        station_id += 1
                else:
                    t_line[row['line']] = {'id': line_id, 'station': {row['name']: station_id}}
                    station_list.append([z_row['sub_area_id'], line_id, row['line'], station_id, row['name']])
                    station_id += 1
                    line_id += 1

    cur = conn.cursor()
    cur.executemany(sql, station_list)
    conn.commit()


if __name__ == '__main__':
    main()