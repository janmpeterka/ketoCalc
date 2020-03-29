"""empty message

Revision ID: fcffcb21448e
Revises: cd8b44186600
Create Date: 2020-03-29 20:28:49.956588

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "fcffcb21448e"
down_revision = "cd8b44186600"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "fk_users_has_diets_diets1", "users_has_diets", type_="foreignkey"
    )
    op.drop_constraint(
        "fk_users_has_diets_users1", "users_has_diets", type_="foreignkey"
    )
    op.drop_index("ix_users_has_diets_diet_id", table_name="users_has_diets")
    op.drop_index("ix_users_has_diets_user_id", table_name="users_has_diets")
    op.drop_table("users_has_diets")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users_has_diets",
        sa.Column(
            "user_id",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "diet_id",
            mysql.INTEGER(display_width=11),
            autoincrement=False,
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["diet_id"], ["diets.id"], name="fk_users_has_diets_diets1"
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name="fk_users_has_diets_users1"
        ),
        sa.PrimaryKeyConstraint("user_id", "diet_id"),
        mysql_default_charset="utf8",
        mysql_engine="InnoDB",
    )
    op.create_index(
        "ix_users_has_diets_user_id", "users_has_diets", ["user_id"], unique=False
    )
    op.create_index(
        "ix_users_has_diets_diet_id", "users_has_diets", ["diet_id"], unique=False
    )
    # ### end Alembic commands ###
