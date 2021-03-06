"""Remove public recipes

Revision ID: d6fa11386771
Revises: 74dd49bc5c76
Create Date: 2020-01-19 13:46:02.976075

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "d6fa11386771"
down_revision = "74dd49bc5c76"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("recipes", "is_public")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "recipes",
        sa.Column(
            "is_public",
            mysql.TINYINT(display_width=1),
            server_default=sa.text("'0'"),
            autoincrement=False,
            nullable=False,
        ),
    )
    # ### end Alembic commands ###
