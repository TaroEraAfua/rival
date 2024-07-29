"""Add team_members table

Revision ID: 1722225534142
Revises: 
Create Date: 2023-04-28 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1722225534142'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'team_members',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('created_at', sa.DateTime, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime, default=sa.func.now(), onupdate=sa.func.now()),
        sa.Column('team_id', sa.String(255), sa.ForeignKey('teams.team_id'), nullable=False),
        sa.Column('user_id', sa.String(255), sa.ForeignKey('users.user_id'), nullable=False),
        sa.Column('is_admin', sa.Boolean, default=False),
        sa.Column('join_date', sa.DateTime, default=sa.func.now()),
    )


def downgrade():
    op.drop_table('team_members')