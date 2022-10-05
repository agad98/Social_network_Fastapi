"""Create posts table

Revision ID: 41a797dbe38a
Revises: 
Create Date: 2022-10-04 16:34:27.602076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41a797dbe38a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.create_table('posts', sa.Column('id', sa.INTEGER(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))

    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
