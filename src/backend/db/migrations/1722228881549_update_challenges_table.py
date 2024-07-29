"""Update challenges table

Revision ID: 1722228881549
Revises: 
Create Date: 2023-04-28 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1722228881549'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Assuming the 'challenges' table already exists
    # Add new columns to the 'challenges' table
    op.add_column('challenges', sa.Column('new_column_name', sa.String(255), nullable=True))
    # Repeat the above line for each new column needed, with the appropriate column name and type
    # Add any new foreign key constraints
    # op.create_foreign_key('fk_challenges_teams', 'challenges', 'teams', ['team_id'], ['team_id'])
    # op.create_foreign_key('fk_challenges_chats', 'challenges', 'chats', ['challenge_id'], ['challenge_id'])
    # Note: The above foreign key creation lines are commented out because the exact columns and table names need to be confirmed


def downgrade():
    # Remove new columns from the 'challenges' table
    op.drop_column('challenges', 'new_column_name')
    # Repeat the above line for each new column added in the upgrade function
    # Note: Do not remove foreign key constraints here, as it's not safe to do so without knowing the exact state of the database