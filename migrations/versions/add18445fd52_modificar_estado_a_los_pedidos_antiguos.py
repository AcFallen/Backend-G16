"""modificar estado a los pedidos antiguos

Revision ID: add18445fd52
Revises: 6935ccb00328
Create Date: 2024-02-08 19:39:02.018005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add18445fd52'
down_revision = '6935ccb00328'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("UPDATE pedidos SET estado = 'EN_ESPERA'")

def downgrade():
    pass
