# from models import Product

# Simulated in-memory storage
product_db = {}

def create_product(product: Product) -> Product:
    product_db[product.id] = product
    return product

def get_product_by_id(product_id: int) -> Product | None:
    return product_db.get(product_id)
