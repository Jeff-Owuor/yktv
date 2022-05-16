"""Fourth Migration

Revision ID: 4735f02c3d91
Revises: 561819a8985e
Create Date: 2022-05-16 17:12:59.059305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4735f02c3d91'
down_revision = '561819a8985e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'author')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('author', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
