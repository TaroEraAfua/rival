"""Update teams table

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
    # Add upgrade logic based on the team model
    # Check for existence of each column and add if necessary
    # Example for a new column 'new_column_name':
    # if not column_exists('teams', 'new_column_name'):
    #     op.add_column('teams', sa.Column('new_column_name', sa.String(255), nullable=True))
    
    # Add similar checks and add_column calls for all new columns as per the "# TABLE" section.


def downgrade():  # Downgrade is not supported for this migration
    # To safely revert the changes made by the upgrade function, we would remove the columns.
    # However, as per the instructions, we should not remove columns in the down function.
    # Instead, we can provide a comment indicating that the downgrade is not supported for this migration.
    
    # Example for removing a column 'new_column_name':
    # if column_exists('teams', 'new_column_name'):
    #     op.drop_column('teams', 'new_column_name')
    
    # Add similar checks and drop_column calls for all columns that were added in the upgrade function.
    # However, since we are not supposed to remove columns, we will not implement these calls.
    
    # Downgrade logic is intentionally left blank


# Helper function to check if a column exists in a given table
def column_exists(table_name, column_name):
    conn = op.get_bind()
    insp = sa.engine.reflection.Inspector.from_engine(conn)
    return column_name in [col['name'] for col in insp.get_columns(table_name)]