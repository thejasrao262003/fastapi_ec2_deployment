from fastapi import APIRouter, HTTPException
from models import Product
from services.product_service import create_product, get_product_by_id

router = APIRouter()

@router.post("/", response_model=Product)
def create(product: Product):
    return create_product(product)

@router.get("/{product_id}", response_model=Product)
def get(product_id: int):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
