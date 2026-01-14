"""short_urls_change_primary_key

Revision ID: e5bfde6bbcb1
Revises: 078eeab56812
Create Date: 2026-01-11 09:13:32.748807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e5bfde6bbcb1'
down_revision: Union[str, Sequence[str], None] = '078eeab56812'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('short_urls', 'id')


def downgrade() -> None:
    op.add_column('short_urls', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
