"""changed field names, Pitch body and backref to authors

Revision ID: 933b07b38a47
Revises: 62db01903071
Create Date: 2018-05-18 21:10:12.975181

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '933b07b38a47'
down_revision = '62db01903071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('author_id', sa.Integer(), nullable=False))
    op.drop_constraint('comments_user_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'users', ['author_id'], ['id'])
    op.drop_column('comments', 'user_id')
    op.add_column('pitches', sa.Column('author_id', sa.Integer(), nullable=False))
    op.add_column('pitches', sa.Column('body', sa.Text(), nullable=True))
    op.add_column('pitches', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_pitches_body'), 'pitches', ['body'], unique=False)
    op.drop_index('ix_pitches_title', table_name='pitches')
    op.drop_constraint('pitches_user_fkey', 'pitches', type_='foreignkey')
    op.create_foreign_key(None, 'pitches', 'users', ['author_id'], ['id'])
    op.drop_column('pitches', 'user')
    op.drop_column('pitches', 'title')
    op.drop_column('pitches', 'created_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('user', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.create_foreign_key('pitches_user_fkey', 'pitches', 'users', ['user'], ['id'])
    op.create_index('ix_pitches_title', 'pitches', ['title'], unique=False)
    op.drop_index(op.f('ix_pitches_body'), table_name='pitches')
    op.drop_column('pitches', 'timestamp')
    op.drop_column('pitches', 'body')
    op.drop_column('pitches', 'author_id')
    op.add_column('comments', sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_user_id_fkey', 'comments', 'users', ['user_id'], ['id'])
    op.drop_column('comments', 'author_id')
    # ### end Alembic commands ###
