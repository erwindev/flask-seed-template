"""sample table

Revision ID: 94b597e59a79
Revises:
Create Date: 2017-06-19 17:56:44.317766

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '94b597e59a79'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('temp_table',
    sa.Column('id', postgresql.UUID(), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('temp_table')
    # ### end Alembic commands ###
