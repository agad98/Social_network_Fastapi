"""Add content column to posts table

Revision ID: e7f2d32e1975
Revises: 41a797dbe38a
Create Date: 2022-10-04 16:50:57.095572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7f2d32e1975'
down_revision = '41a797dbe38a'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
