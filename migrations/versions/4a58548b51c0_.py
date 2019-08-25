"""empty message

Revision ID: 4a58548b51c0
Revises: 83f59531395c
Create Date: 2019-08-24 22:13:44.368787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a58548b51c0'
down_revision = '83f59531395c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('drift', sa.Column('pending', sa.SmallInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('drift', 'pending')
    # ### end Alembic commands ###
