"""rename address

Revision ID: 123f4a2ffbfe
Revises: 80a231e832a4
Create Date: 2025-01-16 02:41:20.864185

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '123f4a2ffbfe'
down_revision = '80a231e832a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
