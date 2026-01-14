"""add_short_url_visitors_field

Revision ID: 078eeab56812
Revises: d25b0d05a95e
Create Date: 2026-01-09 12:20:28.853205

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = '078eeab56812'
down_revision: str | Sequence[str] | None = 'd25b0d05a95e'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column('short_urls', sa.Column('visitors', sa.Integer(), server_default=sa.text('0'), nullable=False))


def downgrade() -> None:
    op.drop_column('short_urls', 'visitors')
