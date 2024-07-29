create table add_team
(
	u_add_id varchar(255) not null,
	team_id varchar(255) not null,
	user_id varchar(255) not null,
	message varchar(255) null,
	status tinyint(1) null,
	register_dt date null,
	primary key (u_add_id, team_id, user_id)
)
charset=utf8;

create table challenge_chat_log
(
	challenge_id varchar(255) not null,
	log_no int not null,
	send_team_id varchar(255) not null,
	send_user_id varchar(255) not null,
	message text null,
	register_dt date null,
	update_time datetime null,
	constraint challenge_id
		unique (challenge_id, log_no, send_team_id)
)
charset=utf8;

alter table challenge_chat_log
	add primary key (challenge_id, log_no, send_team_id);

create table city_master
(
	prefecture_id varchar(255) not null,
	city_id varchar(255) not null,
	city_name varchar(255) not null,
	city_level float null,
	update_time datetime null,
	primary key (prefecture_id, city_id)
)
charset=utf8;

create table const_master
(
	const_id varchar(255) not null,
	const_name varchar(255) not null,
	const_sub_id tinyint not null,
	const_sub_name varchar(255) not null,
	primary key (const_id, const_sub_id)
)
charset=utf8;

create table join_chat_log
(
	chat_id varchar(255) not null,
	log_no int not null,
	send_team_id varchar(255) not null,
	message text null,
	register_dt date null,
	update_time datetime null,
	primary key (chat_id, log_no, send_team_id)
)
charset=utf8;

create table jointy_info
(
	chat_id varchar(255) not null,
	team_id varchar(255) not null,
	user_id varchar(255) not null,
	status tinyint(1) not null,
	register_dt date null,
	primary key (chat_id, team_id, user_id)
)
charset=utf8;

create table mail_template
(
	mail_id int not null
		primary key,
	from_add varchar(255) null,
	from_pass varchar(255) null,
	subject text null,
	body longtext null
);

create table prefectures_master
(
	prefecture_id varchar(255) not null
		primary key,
	prefecture_name varchar(255) not null
)
charset=utf8;

create table station_master
(
	prefecture_id varchar(255) not null,
	line_id varchar(255) not null,
	line_name varchar(255) not null,
	station_id varchar(255) not null,
	station_name varchar(255) not null,
	address text not null,
	primary key (prefecture_id, line_id, station_id)
)
charset=utf8;

create table t_challenge
(
	challenge_id varchar(255) not null,
	team_id varchar(255) not null,
	game_date date not null,
	game_time_start time not null,
	send_team_id varchar(255) not null,
	challenge_status int null,
	register_dt date null,
	update_time datetime null,
	primary key (challenge_id, team_id, game_date, send_team_id, game_time_start)
)
charset=utf8;

create table t_feature
(
	team_id varchar(255) not null,
	feature_id tinyint(3) not null,
	register_dt date null,
	primary key (team_id, feature_id)
)
charset=utf8;

create table t_game_date
(
	team_id varchar(255) not null,
	game_date date not null,
	game_time_start time not null,
	game_time_end time null,
	comment text null,
	game_status tinyint(1) default 0 null,
	challenge_id varchar(255) null,
	register_dt date null,
	update_time datetime null,
	primary key (team_id, game_date, game_time_start)
)
charset=utf8;

create table t_level
(
	team_id varchar(255) not null
		primary key,
	level int null,
	experience float null,
	win_count int null,
	register_dt date null,
	update_time datetime null
)
charset=utf8;

create table t_purpose
(
	team_id varchar(255) not null,
	purpose_id varchar(255) not null,
	register_dt date null,
	update_time datetime null,
	primary key (team_id, purpose_id)
)
charset=utf8;

create table t_week
(
	team_id varchar(255) not null,
	week_id varchar(255) not null,
	time_id varchar(255) not null,
	register_dt date null,
	update_time datetime null,
	primary key (team_id, week_id, time_id)
)
charset=utf8;

create table team_info
(
	team_id varchar(255) not null,
	user_id varchar(255) not null,
	admin tinyint(1) null,
	register_dt date null,
	update_time datetime null,
	default_flg tinyint(1) default 0 not null,
	primary key (team_id, user_id)
)
charset=utf8;

create table team_profile
(
	team_id varchar(255) not null
		primary key,
	team_name varchar(255) not null,
	team_image varchar(255) null,
	prefecture_id varchar(255) not null,
	city_id varchar(255) null,
	line_id varchar(255) null,
	station_id varchar(255) null,
	avg_age int not null,
	gym tinyint(1) not null,
	solicitation_flg tinyint(1) not null,
	stray_flg tinyint(1) not null,
	main_place varchar(255) null,
	member_num int null,
	gender tinyint(1) null,
	c_comment text null,
	u_comment text null,
	register_dt date null,
	update_time datetime null
)
charset=utf8;

create table token
(
	token_id varchar(32) not null
		primary key,
	user_id varchar(255) null,
	regist_dt datetime not null
);

create table u_ex_width
(
	user_id varchar(255) not null,
	width_id tinyint(1) not null,
	register_dt date null,
	primary key (user_id, width_id)
)
charset=utf8;

create table u_favorite
(
	user_id varchar(255) not null,
	team_id int not null,
	register_dt date null,
	update_time datetime null,
	primary key (user_id, team_id)
)
charset=utf8;

create table u_position
(
	user_id varchar(255) not null,
	position_id tinyint(1) not null,
	register_dt date null,
	update_time datetime null,
	primary key (user_id, position_id)
)
charset=utf8;

create table u_week
(
	user_id varchar(255) not null,
	week_id varchar(255) not null,
	time_id varchar(255) not null,
	register_dt date null,
	update_time datetime null,
	primary key (user_id, week_id, time_id)
)
charset=utf8;

create table user_info
(
	user_id varchar(255) not null
		primary key,
	user_name varchar(255) not null,
	password varchar(255) not null,
	mail text null,
	token_id varchar(32) null,
	owner_num int default 1 null,
	icon varchar(255) not null,
	ex_year int null,
	height float null,
	sign_in_time datetime null,
	birth_dt date not null,
	prefecture_id varchar(255) not null,
	city_id varchar(255) not null,
	line_id varchar(255) null,
	station_id varchar(255) null,
	gender int null,
	comment text null,
	register_dt date null,
	update_time datetime null
)
charset=utf8;

