"""Added canvas_data column to room table

Revision ID: b7a00185e0fa
Revises: b5cfccfdbaf0
Create Date: 2024-10-19 01:30:33.326344

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7a00185e0fa'
down_revision: Union[str, None] = 'b5cfccfdbaf0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
