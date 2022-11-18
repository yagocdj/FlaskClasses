"""first migration

Revision ID: 7afd5b969dad
Revises: 
Create Date: 2022-11-18 11:26:25.941923

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7afd5b969dad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppy')
    # ### end Alembic commands ###
