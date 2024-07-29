# coding: utf-8
import pymysql.cursors
import pandas as pd



def main():
    conn = con_mysql()
    set_station(conn)


def con_mysql():
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='rival',
                           cursorclass=pymysql.cursors.DictCursor)
    return conn


def set_station(conn):
    sql = '''
                insert into station_master 
                    (prefecture_id, line_id, station_id, station_name, address, line_name) 
                VALUES (%s, %s, %s, %s, %s, %s)
           '''
    df_line = pd.read_csv('line20180424free.csv', encoding='utf-8', dtype=str, usecols=['line_cd', 'line_name'])
    df_station = pd.read_csv('station20180330free.csv', encoding='utf-8', dtype=str, usecols=['line_cd', 'pref_cd', 'station_cd', 'station_name', 'add'])
    df_station = df_station.ix[:, ['pref_cd', 'line_cd', 'station_cd', 'station_name', 'add']]
    cur = conn.cursor()
    tmp = []

    for row in df_station.values.tolist():
        if len(row[0]) == 1:
            row[0] = '0' + row[0]
        df_exact = df_line[df_line['line_cd'] == row[1]]
        df_exact = df_exact.reset_index(drop=True)
        row.append(df_exact.loc[0]['line_name'])
        tmp.append(row)
    cur.executemany(sql, tmp)
    conn.commit()


if __name__ == '__main__':
    main()