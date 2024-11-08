"""add dementia daycare and review models

Revision ID: f838cdfa6d82
Revises: da7410cd3ba2
Create Date: 2024-11-08 13:04:38.000031

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f838cdfa6d82'
down_revision: Union[str, None] = 'da7410cd3ba2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dementia_daycare',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('friendly_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('website', sa.String(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.Column('operating_hours', postgresql.ARRAY(sa.String()), nullable=False),
    sa.Column('building_name', sa.String(), nullable=True),
    sa.Column('block', sa.String(), nullable=True),
    sa.Column('postal_code', sa.String(), nullable=False),
    sa.Column('street_name', sa.String(), nullable=True),
    sa.Column('unit_no', sa.String(), nullable=True),
    sa.Column('availability', sa.String(), nullable=True),
    sa.Column('google_map_place_id', sa.String(), nullable=False),
    sa.Column('photos', postgresql.ARRAY(sa.String()), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('friendly_id')
    )
    op.create_index(op.f('ix_dementia_daycare_id'), 'dementia_daycare', ['id'], unique=True)
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('review_target', sa.Enum('CARESERVICE::DEMENTIA_DAYCARE', name='reviewable'), nullable=False),
    sa.Column('review_target_id', sa.Integer(), nullable=False),
    sa.Column('review_source', sa.Enum('GOOGLE', 'IN_APP', name='reviewsource'), nullable=False),
    sa.Column('author_name', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('overall_rating', sa.Integer(), nullable=False),
    sa.Column('published_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reviews_id'), 'reviews', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reviews_id'), table_name='reviews')
    op.drop_table('reviews')
    op.drop_index(op.f('ix_dementia_daycare_id'), table_name='dementia_daycare')
    op.drop_table('dementia_daycare')
    op.execute('DROP TYPE reviewsource')
    op.execute('DROP TYPE reviewable')
    # ### end Alembic commands ###