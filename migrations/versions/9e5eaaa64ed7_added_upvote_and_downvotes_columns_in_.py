"""added upvote and downvotes columns in the pitch model

Revision ID: 9e5eaaa64ed7
Revises: c1d05f77a5ab
Create Date: 2018-05-20 09:58:42.178958

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e5eaaa64ed7'
down_revision = 'c1d05f77a5ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vote')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vote',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('vote', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], name='vote_author_id_fkey'),
    sa.ForeignKeyConstraint(['pitch_id'], ['pitches.id'], name='vote_pitch_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='vote_pkey')
    )
    # ### end Alembic commands ###