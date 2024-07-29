from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from .base import Base

class TeamMember(Base):
    __tablename__ = 'team_members'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    team_id = Column(String(255), ForeignKey('teams.team_id'), nullable=False)
    user_id = Column(String(255), ForeignKey('users.user_id'), nullable=False)
    is_admin = Column(Boolean, default=False)
    join_date = Column(DateTime, default=datetime.utcnow)

    def __init__(self, team_id, user_id, is_admin=False):
        self.team_id = team_id
        self.user_id = user_id
        self.is_admin = is_admin