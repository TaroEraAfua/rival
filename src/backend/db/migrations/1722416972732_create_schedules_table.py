from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    schedules = Table(
        'schedules', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('created_at', DateTime, default=datetime.utcnow),
        Column('updated_at', DateTime, default=datetime.utcnow, onupdate=datetime.utcnow),
        Column('schedule_id', String(255), nullable=False),
        Column('title', String(255), nullable=False),
        Column('description', String(255), nullable=True),
        Column('start_time', DateTime, nullable=False),
        Column('end_time', DateTime, nullable=False),
        Column('register_dt', DateTime, nullable=False),
        Column('update_time', DateTime, nullable=False),
        Column('user_id', Integer, ForeignKey('users.user_id')),
    )
    schedules.create()

def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine, reflect=True)
    schedules = Table('schedules', meta, autoload=True)
    schedules.drop()