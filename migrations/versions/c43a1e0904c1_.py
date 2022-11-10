"""empty message

Revision ID: c43a1e0904c1
Revises: 
Create Date: 2022-11-10 02:08:23.045276

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c43a1e0904c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goal',
    sa.Column('goal_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('goal_id')
    )
    op.add_column('task', sa.Column('is_completed', sa.Boolean(), nullable=True))
    op.drop_column('task', 'completed_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('completed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('task', 'is_completed')
    op.drop_table('goal')
    # ### end Alembic commands ###