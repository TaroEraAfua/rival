from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import and_
from .database import Base
from datetime import datetime

class Schedule(Base):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    schedule_id = Column(String(255), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    register_dt = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    user = relationship("User", back_populates="schedules")

    def check_conflicts(self, user_id, start_time, end_time):
        overlapping_schedules = Schedule.query.filter(
            Schedule.user_id == user_id,
            and_(
                Schedule.start_time < end_time,
                Schedule.end_time > start_time
            )
        ).first()
        return overlapping_schedules is not None