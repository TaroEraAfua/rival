# coding: utf-8
from api.model.const import Const
from api.model.area import Area
import base64
import os
import api.common.unit as format
import api.common.constant as constant
from api.common.unit import debug_log


def get_const_data():
    c_list = Const.get_const()
    result = {}
    img_path = os.path.dirname(os.path.abspath(__file__))
    img_path = img_path.replace('controller', 'icon') + '/'

    pre_name = ''

    try:
        for row in c_list:
            tmp = row.to_dict()
            if tmp['const_name'] == 'icon':
                img = img_path + tmp['const_sub_name']
                with open(img, "rb") as f:
                    tmp['icon'] = 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')
            if pre_name == '':
                result[tmp['const_name']] = [{
                    'id': tmp['const_sub_id'],
                    'label': tmp['const_sub_name'],
                    'val': tmp['icon'] if 'icon' in tmp else tmp['const_sub_id'],
                    'item': tmp
                    }]
            if pre_name == tmp['const_name']:
                result[tmp['const_name']].append({
                    'id': tmp['const_sub_id'],
                    'label': tmp['const_sub_name'],
                    'val': tmp['icon'] if 'icon' in tmp else tmp['const_sub_id'],
                    'item': tmp
                    })
            else:
                result[tmp['const_name']] = [{
                    'id': tmp['const_sub_id'],
                    'label': tmp['const_sub_name'],
                    'val': tmp['icon'] if 'icon' in tmp else tmp['const_sub_id'],
                    'item': tmp
                    }]
            pre_name = tmp['const_name']
        response = format.format_return_param(constant.RESULT_CODE_OK, constant.MESSAGE_OK_001, result)
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def get_prefecture():
    res = Area.get_prefecture()

    prefecture = []
    try:
        for val in res:
            t = {'label': val['prefecture_name'], 'val': val['prefecture_id'],'item': val}
            prefecture.append(t)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            {'prefecture': prefecture}
        )
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def get_city(prefecture_id):
    res = Area.get_city(prefecture_id)
    city = []
    try:
        for val in res:
            t = {'label': val['city_name'], 'val': val['city_id'], 'item': val}
            city.append(t)
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            {'city': city}
        )
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response


def get_station(prefecture_id, city_name):
    res = Area.get_station(prefecture_id, city_name)
    station = []
    idx = 0
    try:
        for val in res:
            t = { 'val': idx, 'label': val['line_name'] + ' - ' + val['station_name'], 'item': val}
            station.append(t)
            idx += 1
        response = format.format_return_param(
            constant.RESULT_CODE_OK,
            constant.MESSAGE_OK_001,
            {'station': station}
        )
    except Exception as e:
        response = format.format_return_param(
            constant.RESULT_CODE_ERR_SYSTEM,
            constant.MESSAGE_ERR_SYSTEM
        )

    return response
