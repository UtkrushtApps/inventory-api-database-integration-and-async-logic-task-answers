# Solution Steps

1. Design the PostgreSQL products table with fields: id (PK), name, sku (unique), description, price, quantity, created_at, using proper types, uniqueness, and indexes.

2. Create an Alembic migration file to create the products table as designed, with all relevant columns, unique constraints (on SKU), and indexes.

3. Implement the SQLAlchemy ORM Product model in models.py reflecting the products table schema, including uniqueness on sku and proper types.

4. Set up the asynchronous database connection and session in database.py using SQLAlchemy's async engine, and provide an async get_db dependency function.

5. Implement async CRUD functions in crud.py: (a) create_product to insert a new product using async session, enforcing SKU uniqueness (return None on IntegrityError); (b) get_products to fetch all products asynchronously.

6. Integrate models and async database logic with FastAPI: in the route handlers (already implemented), use get_db to acquire sessions and call the CRUD functions for adding and retrieving products.

