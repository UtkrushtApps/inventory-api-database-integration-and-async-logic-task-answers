from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select
from sqlalchemy import insert
from models import Product
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional, Dict, Any

async def create_product(db: AsyncSession, product_data: Dict[str, Any]) -> Optional[Product]:
    try:
        db_product = Product(**product_data)
        db.add(db_product)
        await db.commit()
        await db.refresh(db_product)
        return db_product
    except IntegrityError:
        await db.rollback()
        return None

async def get_products(db: AsyncSession) -> List[Product]:
    result = await db.execute(select(Product))
    return result.scalars().all()
