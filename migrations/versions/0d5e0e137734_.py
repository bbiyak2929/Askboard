"""empty message

Revision ID: 0d5e0e137734
Revises: 3f78f53d2d86
Create Date: 2023-08-07 23:00:48.286637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d5e0e137734'
down_revision = '3f78f53d2d86'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_answer_user_id_user'), 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_answer_user_id_user'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
