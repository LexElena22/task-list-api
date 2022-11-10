"""empty message

Revision ID: 6e5738d80435
Revises: 83475dc44270
Create Date: 2022-11-10 09:38:22.992482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e5738d80435'
down_revision = '83475dc44270'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('completed_at', sa.DateTime(), nullable=True))
    op.drop_column('task', 'is_complete')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('is_complete', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('task', 'completed_at')
    # ### end Alembic commands ###