from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

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
    user_id = Column(Integer, ForeignKey('users.user_id'), index=True)

    user = relationship("User", back_populates="schedules", foreign_keys=[user_id])