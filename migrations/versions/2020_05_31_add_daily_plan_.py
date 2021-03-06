"""Adds daily plans

Revision ID: a157327dd8c5
Revises: a8a0fbdf5043
Create Date: 2020-05-31 23:07:36.193024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a157327dd8c5"
down_revision = "a8a0fbdf5043"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "daily_plans",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_daily_plans_user_id"), "daily_plans", ["user_id"], unique=False
    )
    op.create_table(
        "daily_plan_has_recipes",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("recipes_id", sa.Integer(), nullable=False),
        sa.Column("daily_plans_id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("added_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["daily_plans_id"], ["daily_plans.id"],),
        sa.ForeignKeyConstraint(["recipes_id"], ["recipes.id"],),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_daily_plan_has_recipes_daily_plans_id"),
        "daily_plan_has_recipes",
        ["daily_plans_id"],
        unique=False,
    )
    op.create_index(
        op.f("ix_daily_plan_has_recipes_recipes_id"),
        "daily_plan_has_recipes",
        ["recipes_id"],
        unique=False,
    )


def downgrade():
    # op.drop_index(
    # op.f("ix_daily_plan_has_recipes_recipes_id"),
    # table_name="daily_plan_has_recipes",
    # )
    # op.drop_index(
    # op.f("ix_daily_plan_has_recipes_daily_plans_id"),
    # table_name="daily_plan_has_recipes",
    # )
    op.drop_table("daily_plan_has_recipes")
    # op.drop_index(op.f("ix_daily_plans_user_id"), table_name="daily_plans")
    op.drop_table("daily_plans")
