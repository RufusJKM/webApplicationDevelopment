"""empty message

Revision ID: 436be2ca52a6
Revises: 7dd5eaa201ef
Create Date: 2024-11-22 13:34:21.012309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '436be2ca52a6'
down_revision = '7dd5eaa201ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.create_unique_constraint('email', ['email'])
        batch_op.drop_column('phone_number')

    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('basket_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('order_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_order_id', 'order', ['order_id'], ['id'])
        batch_op.create_foreign_key('fk_basket_id', 'basket', ['basket_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_constraint('fk_order_id', type_='foreignkey')
        batch_op.drop_constraint('fk_basket_id', type_='foreignkey')
        batch_op.drop_column('order_id')
        batch_op.drop_column('basket_id')

    with op.batch_alter_table('customer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', sa.VARCHAR(length=20), nullable=True))
        batch_op.drop_constraint('phone_number', type_='unique')

    op.drop_table('order')
    # ### end Alembic commands ###