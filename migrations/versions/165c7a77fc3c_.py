"""empty message

Revision ID: 165c7a77fc3c
Revises: 30804e4fff58
Create Date: 2018-09-19 15:46:31.640047

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '165c7a77fc3c'
down_revision = '30804e4fff58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('humid_sensors', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('temp_sensors', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'temp_sensors')
    op.drop_column('user', 'humid_sensors')
    # ### end Alembic commands ###
