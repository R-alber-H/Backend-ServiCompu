from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate

class ProductService():
    def __init__(self,repo_product:ProductRepository):
        self.repo_product = repo_product
        
    def create_product(self,product:ProductCreate):
        exists_product = self.repo_product.get_by_name(product.name)
        if exists_product:
            raise ValueError("El producto ya esta registrado")
        new_product = Product(
            name = product.name,
            price = product.price,
            img_url = product.img_url,
            description = product.description,
            brand_id = product.brand_id,
            supplier_id = product.supplier_id
        )
        return self.repo_product.create_product(new_product,product.initial_stock,product.category_ids)
    
    def get_all(self):
        return self.repo_product.get_all()
    
    def get_by_id(self,id:int):
        product = self.repo_product.get_by_id(id)
        if not product:
            raise ValueError(f"El producto con id {id} no esta registrado")
        return product