
CREATE TABLE `const_master` (
 `const_id` VARCHAR(255) NOT NULL
, `const_name` VARCHAR(255) NOT NULL
, `const_sub_id` tinyint(4) NOT NULL
, `const_sub_name` VARCHAR(255) NOT NULL
, PRIMARY KEY (`const_id`, `const_sub_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `prefectures_master` (
 `prefecture_id` VARCHAR(255) NOT NULL
, `prefecture_name` VARCHAR(255) NOT NULL
, PRIMARY KEY (`prefecture_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `city_master` (
 `prefecture_id` VARCHAR(255) NOT NULL
, `city_id` VARCHAR(255) NOT NULL
, `city_name` VARCHAR(255) NOT NULL
, `city_level` float 
, `update_time` datetime
, PRIMARY KEY (`prefecture_id`, `city_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `team_info` (
 `team_id` VARCHAR(255) NOT NULL
, `user_id` VARCHAR(255) NOT NULL
, `admin` tinyint(1) 
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`team_id`, `user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `team_profile` (
 `team_id` VARCHAR(255) NOT NULL
, `team_name` VARCHAR(255) NOT NULL
, `team_image` VARCHAR(255) 
, `prefecture_id` VARCHAR(255) NOT NULL
, `city_id` VARCHAR(255) 
, `line_id` VARCHAR(255) 
, `station_id` VARCHAR(255) 
, `avg_age` tinyint(1) NOT NULL
, `gym` tinyint(1) NOT NULL
, `solicitation_flg` tinyint(1) NOT NULL
, `stray_flg` tinyint(1) NOT NULL
, `main_place` VARCHAR(255)
, `member_num` int
, `gender` tinyint(1)
, `c_comment` text 
, `u_comment` text 
, `register_dt` date 
, `update_time` datetime 
, PRIMARY KEY (`team_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_week` (
 `team_id` VARCHAR(255) NOT NULL
, `week_id` VARCHAR(255) NOT NULL
, `time_id` VARCHAR(255) NOT NULL
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`team_id`, `week_id`, `time_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_feature` (
 `team_id` VARCHAR(255) NOT NULL
, `feature_id` tinyint(3) NOT NULL
, `register_dt` date
, PRIMARY KEY (`team_id`, `feature_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_game_date` (
 `team_id` VARCHAR(255) NOT NULL
, `game_date` date NOT NULL
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`team_id`, `game_date`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `station_master` (
 `prefecture_id` VARCHAR(255) NOT NULL
, `line_id` VARCHAR(255) NOT NULL
, `line_name` VARCHAR(255) NOT NULL
, `station_id` VARCHAR(255) NOT NULL
, `station_name` VARCHAR(255) NOT NULL
, `address` text NOT NULL
, PRIMARY KEY (`prefecture_id`, `line_id`, `station_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_purpose` (
 `team_id` VARCHAR(255) NOT NULL
, `purpose_id` VARCHAR(255) NOT NULL
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`team_id`, `purpose_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_level` (
 `team_id` VARCHAR(255) NOT NULL
, `level` int 
, `experience` float 
, `win_count` int 
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`team_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `t_challenge` (
 `challenge_id` VARCHAR(255) NOT NULL
, `send_team_id` VARCHAR(255) NOT NULL
, `res_team_id` VARCHAR(255) NOT NULL
, `status` int 
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`challenge_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `challenge_chat_log` (
 `challenge_id` VARCHAR(255) NOT NULL
, `log_no` int NOT NULL
, `send_team_id` VARCHAR(255) NOT NULL
, `message` text 
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`challenge_id`, `log_no`, `send_team_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `user_info` (
 `user_id` VARCHAR(255) NOT NULL
,`user_name` VARCHAR(255) NOT NULL
, `password` VARCHAR(255) NOT NULL
, `g_token` longtext
, `icon` VARCHAR(255) NOT NULL
, `ex_year` int 
, `height` float 
, `sign_in_time` datetime 
, `birth_dt` date NOT NULL
, `prefecture_id` VARCHAR(255) NOT NULL
, `city_id` VARCHAR(255) NOT NULL
, `gender` int 
, `comment` text 
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `add_team` (
 `u_add_id` VARCHAR(255) NOT NULL
, `team_id` VARCHAR(255) NOT NULL
, `user_id` VARCHAR(255) NOT NULL
, `message` VARCHAR(255) 
, `status` tinyint(1) 
, `register_dt` date
, PRIMARY KEY (`u_add_id`, `team_id`, `user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `u_ex_width` (
 `user_id` VARCHAR(255) NOT NULL
, `width_id` tinyint(1) NOT NULL
, `register_dt` date
, PRIMARY KEY (`user_id`, `width_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `jointy_info` (
 `chat_id` VARCHAR(255) NOT NULL
, `t_user_id` VARCHAR(255) NOT NULL
, `user_id` VARCHAR(255) NOT NULL
, `status` tinyint(1) NOT NULL
, `register_dt` date
, PRIMARY KEY (`chat_id`, `t_user_id`, `user_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `join_chat_log` (
 `chat_id` VARCHAR(255) NOT NULL
, `log_no` int NOT NULL
, `send_team_id` VARCHAR(255) NOT NULL
, `message` text 
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`chat_id`, `log_no`, `send_team_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `u_favorite` (
 `user_id` VARCHAR(255) NOT NULL
, `team_id` int NOT NULL
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`user_id`, `team_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `u_position` (
 `user_id` VARCHAR(255) NOT NULL
, `position_id` tinyint(1)
, `register_dt` date 
, `update_time` datetime
, PRIMARY KEY (`user_id`, `position_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `u_week` (
 `user_id` VARCHAR(255) NOT NULL
, `week_id` VARCHAR(255) NOT NULL
, `time_id` VARCHAR(255) NOT NULL
, `register_dt` date
, `update_time` datetime
, PRIMARY KEY (`user_id`, `week_id`, `time_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;