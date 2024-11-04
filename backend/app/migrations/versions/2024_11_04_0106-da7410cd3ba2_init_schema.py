"""init schema

Revision ID: da7410cd3ba2
Revises: 
Create Date: 2024-11-04 01:06:00.809326

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da7410cd3ba2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('clerk_id', sa.String(), nullable=True),
    sa.Column('citizenship', sa.Enum('CITIZEN', 'PR', 'OTHER', name='citizenship'), nullable=True),
    sa.Column('care_recipient_age', sa.Integer(), nullable=True),
    sa.Column('care_recipient_citizenship', sa.Enum('CITIZEN', 'PR', 'OTHER', name='citizenship'), nullable=True),
    sa.Column('care_recipient_residence', sa.Enum('HOME', 'NURSING_HOME_LTCF', 'OTHER', name='residence'), nullable=True),
    sa.Column('care_recipient_relationship', sa.Enum('PARENT', 'SPOUSE', 'OTHER_FAMILY', 'NON_FAMILY', name='relationship'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_clerk_id'), 'users', ['clerk_id'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('threads',
    sa.Column('thread_id', sa.String(), nullable=False),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.clerk_id'], ),
    sa.PrimaryKeyConstraint('thread_id')
    )
    op.create_index(op.f('ix_threads_thread_id'), 'threads', ['thread_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_threads_thread_id'), table_name='threads')
    op.drop_table('threads')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_clerk_id'), table_name='users')
    op.drop_table('users')
    op.execute('DROP TYPE citizenship')
    op.execute('DROP TYPE residence')
    op.execute('DROP TYPE relationship')
    # ### end Alembic commands ###
