"""adds many to many relationship

Revision ID: 1ea32ca7aa4f
Revises: f7efb2f6d56c
Create Date: 2022-11-27 19:20:17.525307

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils.types.uuid import UUIDType

# revision identifiers, used by Alembic.
revision = '1ea32ca7aa4f'
down_revision = 'f7efb2f6d56c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('timeseries_datetime_tag',
    sa.Column('timeseries_id', UUIDType(), nullable=True),
    sa.Column('datetime_tag_id', UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['datetime_tag_id'], ['datetime_tags.id'], ),
    sa.ForeignKeyConstraint(['timeseries_id'], ['timeseries.id'], )
    )
    op.create_table('timeseries_string_tag',
    sa.Column('timeseries_id', UUIDType(), nullable=True),
    sa.Column('string_tag_id', UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['string_tag_id'], ['string_tags.id'], ),
    sa.ForeignKeyConstraint(['timeseries_id'], ['timeseries.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('timeseries_string_tag')
    op.drop_table('timeseries_datetime_tag')
    # ### end Alembic commands ###
