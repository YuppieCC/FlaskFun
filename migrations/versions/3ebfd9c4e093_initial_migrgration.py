"""initial migrgration

Revision ID: 3ebfd9c4e093
Revises: 
Create Date: 2017-01-19 15:00:00.954789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ebfd9c4e093'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Flaskusers', sa.Column('location', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_Flaskusers_location'), 'Flaskusers', ['location'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_Flaskusers_location'), table_name='Flaskusers')
    op.drop_column('Flaskusers', 'location')
    # ### end Alembic commands ###
