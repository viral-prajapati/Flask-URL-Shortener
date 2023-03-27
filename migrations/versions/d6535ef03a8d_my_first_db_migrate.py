"""My first DB migrate

Revision ID: d6535ef03a8d
Revises: 
Create Date: 2023-03-23 10:40:42.869572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6535ef03a8d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sabjis',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.Text(), nullable=True),
    sa.Column('shorted_url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sabjis')
    # ### end Alembic commands ###
