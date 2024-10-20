"""Added canvas_data column to room table

Revision ID: b5cfccfdbaf0
Revises: e16ad218dbc5
Create Date: 2024-10-19 01:21:57.397802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5cfccfdbaf0'
down_revision: Union[str, None] = 'e16ad218dbc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
