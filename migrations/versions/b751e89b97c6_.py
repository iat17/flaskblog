"""empty message

Revision ID: b751e89b97c6
Revises: 95152262afed
Create Date: 2021-02-17 02:10:11.224330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b751e89b97c6'
down_revision = 'cf53ed3c949b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('description', sa.String(length=120), nullable=False),
    sa.Column('body', sa.String(length=1024), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('articles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('body', sa.VARCHAR(length=1024), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('published', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='articles_pkey')
    )
    # ### end Alembic commands ###
