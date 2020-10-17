"""empty message

Revision ID: 46c018428751
Revises: 699a2dcfff0a
Create Date: 2019-07-31 11:44:55.716351

"""
from alembic import op
import sqlalchemy as sa

# from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "46c018428751"
down_revision = "699a2dcfff0a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("new_password_token", sa.String(length=255), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "new_password_token")
    # ### end Alembic commands ###
