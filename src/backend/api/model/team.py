# coding: utf-8
import pymysql
from util.setting import Setting
from sqlalchemy.orm import relationship
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

        self.challenges = relationship("Challenge", backref="team")
        self.team_members = relationship("TeamMember", backref="team")

    # ... rest of the class methods remain unchanged ...