"""Initial migration

Revision ID: 6815730c5d18
Revises: 
Create Date: 2025-06-03 15:57:04.571612

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6815730c5d18'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('companies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(), nullable=False),
    sa.Column('founding_year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dev_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('company_dev',
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('dev_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('fk_company_dev_company_id_companies')),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name=op.f('fk_company_dev_dev_id_devs')),
    sa.PrimaryKeyConstraint('company_id', 'dev_id')
    )
    op.create_table('freebies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.Column('dev_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name=op.f('fk_freebies_company_id_companies')),
    sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name=op.f('fk_freebies_dev_id_devs')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('freebies')
    op.drop_table('company_dev')
    op.drop_table('devs')
    op.drop_table('companies')
    # ### end Alembic commands ###
