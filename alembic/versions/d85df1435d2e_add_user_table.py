"""Add user table

Revision ID: d85df1435d2e
Revises: e7f2d32e1975
Create Date: 2022-10-04 16:56:53.741576

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd85df1435d2e'
down_revision = 'e7f2d32e1975'
branch_labels = None
depends_on = None


def upgrade() -> None: 
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False), sa.Column('email', sa.String(), nullable=False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False), sa.PrimaryKeyConstraint('id'), sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
