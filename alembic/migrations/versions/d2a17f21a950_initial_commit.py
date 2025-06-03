"""initial commit

Revision ID: d2a17f21a950
Revises: 
Create Date: 2025-06-03 18:11:09.154811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2a17f21a950'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "test_table",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("on_vacation", sa.Boolean, default=False),
    )


def downgrade() -> None:
    op.drop_table("test_table")
