"""Enable shared recipes

Revision ID: 82f0a4250028
Revises: 27cf1eba3af3
Create Date: 2020-10-13 15:54:16.162504

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "82f0a4250028"
down_revision = "27cf1eba3af3"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("recipes", sa.Column("is_shared", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("recipes", "is_shared")
    # ### end Alembic commands ###
