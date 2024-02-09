"""agregue valor default al estado

Revision ID: 6935ccb00328
Revises: 189548427402
Create Date: 2024-02-08 19:32:27.979078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6935ccb00328'
down_revision = '189548427402'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(table_name='pedidos', 
                    column_name='estado',
                    server_default='EN_ESPERA')


def downgrade():
    op.alter_column(table_name='pedidos',
                    column_name='estado',
                    server_default=None)
