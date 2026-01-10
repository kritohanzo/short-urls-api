"""add_short_url_visitors_field

Revision ID: 078eeab56812
Revises: d25b0d05a95e
Create Date: 2026-01-09 12:20:28.853205

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '078eeab56812'
down_revision: Union[str, Sequence[str], None] = 'd25b0d05a95e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('short_urls', sa.Column('visitors', sa.Integer(), server_default=sa.text('0'), nullable=False))


def downgrade() -> None:
    op.drop_column('short_urls', 'visitors')
