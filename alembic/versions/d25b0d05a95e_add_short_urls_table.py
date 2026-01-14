"""add short_urls table

Revision ID: d25b0d05a95e
Revises:
Create Date: 2025-12-21 22:00:49.077786

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = 'd25b0d05a95e'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        'short_urls',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('slug', sa.String(), nullable=False),
        sa.Column('source_url', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('short_urls')
