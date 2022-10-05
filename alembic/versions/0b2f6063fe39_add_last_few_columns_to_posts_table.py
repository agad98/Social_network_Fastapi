"""Add last few columns to posts table

Revision ID: 0b2f6063fe39
Revises: 3a7f66cc085c
Create Date: 2022-10-04 17:14:53.884359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b2f6063fe39'
down_revision = '3a7f66cc085c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.BOOLEAN(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
