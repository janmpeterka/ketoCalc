"""empty message

Revision ID: 699a2dcfff0a
Revises:
Create Date: 2019-06-26 17:54:19.427165

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "699a2dcfff0a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("bunkrs")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "bunkrs",
        sa.Column(
            "name",
            mysql.VARCHAR(collation="utf8_unicode_ci", length=255),
            nullable=False,
        ),
        sa.Column(
            "sale_date",
            mysql.VARCHAR(collation="utf8_unicode_ci", length=255),
            nullable=True,
        ),
        sa.Column(
            "katastr",
            mysql.VARCHAR(collation="utf8_unicode_ci", length=255),
            nullable=True,
        ),
        sa.Column(
            "obec",
            mysql.VARCHAR(collation="utf8_unicode_ci", length=255),
            nullable=True,
        ),
        sa.Column(
            "kraj",
            mysql.VARCHAR(collation="utf8_unicode_ci", length=255),
            nullable=True,
        ),
        sa.Column(
            "uzemi",
            mysql.VARCHAR(collation="utf8_unicode_ci", length=255),
            nullable=True,
        ),
        sa.Column(
            "min_sale_price",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column(
            "created_at",
            mysql.DATETIME(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=True,
        ),
        sa.Column(
            "link",
            mysql.VARCHAR(collation="utf8_unicode_ci", length=255),
            nullable=True,
        ),
        sa.Column(
            "offer_type",
            mysql.VARCHAR(collation="utf8_unicode_ci", length=45),
            server_default=sa.text("'\"sale\"'"),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("name"),
        mysql_collate="utf8_unicode_ci",
        mysql_default_charset="utf8",
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###
