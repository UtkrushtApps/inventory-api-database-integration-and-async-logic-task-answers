from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20230605_01'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'products',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('sku', sa.String(length=100), nullable=False, unique=True, index=True),
        sa.Column('description', sa.String(length=1024), nullable=True),
        sa.Column('price', sa.Float, nullable=False),
        sa.Column('quantity', sa.Integer, nullable=False, server_default='0'),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP')),
        sa.UniqueConstraint('sku', name='uq_products_sku'),
    )

def downgrade():
    op.drop_table('products')
