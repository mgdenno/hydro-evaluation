"""adds string tags

Revision ID: 01881833524a
Revises: 58f330a21952
Create Date: 2022-11-25 16:42:39.335891

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy_utils.types.uuid import UUIDType

# revision identifiers, used by Alembic.
revision = '01881833524a'
down_revision = '58f330a21952'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('string_tag_types',
                    sa.Column('name', sa.String(), nullable=False),
                    sa.PrimaryKeyConstraint('name')
                    )
    op.create_table('string_tags',
                    sa.Column('id', UUIDType(), server_default=sa.text(
                        'gen_random_uuid()'), nullable=False),
                    sa.Column('string_tag_type_name',
                              sa.String(), nullable=False),
                    sa.Column('value', sa.String(), nullable=False),
                    sa.ForeignKeyConstraint(['string_tag_type_name'], [
                        'string_tag_types.name'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('string_tag_type_name', 'value')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('string_tags')
    op.drop_table('string_tag_types')
    # ### end Alembic commands ###