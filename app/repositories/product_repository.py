from sqlalchemy.orm import Session, joinedload
from app.models.inventory import Inventory
from app.models.product import Product
from app.models.product_categories import ProductCategory

class ProductRepository:
    def __init__(self, db : Session):
        self.db = db
    
    def create_product(self, product: Product,stock:int, category_ids: list[int]) -> Product:
        self.db.add(product)
        self.db.flush()
        new_inventory = Inventory(
            product_id =product.id,
            stock = stock
        )
        self.db.add(new_inventory)
        for category_id in category_ids:
            new_product_category = ProductCategory(
                product_id = product.id,
                category_id = category_id
            )
            self.db.add(new_product_category)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def get_all(self) -> list[Product]:
        return(
            self.db.query(Product)
            .options(joinedload(Product.brand))
            .options(joinedload(Product.supplier))
            .options(joinedload(Product.inventory))
            .options(joinedload(Product.product_categories).joinedload(ProductCategory.category))
            .all()
        )
    
    def get_by_id (self, id:int) -> Product | None:
        return(
            self.db.query(Product)
            .options(joinedload(Product.brand))
            .options(joinedload(Product.supplier))
            .options(joinedload(Product.inventory))
            .options(joinedload(Product.product_categories).joinedload(ProductCategory.category))
            .filter(Product.id == id)
            .first()
        )
        
    def get_by_name (self,name: str) -> Product | None:
        return(
            self.db.query(Product)
            .filter(Product.name == name)
            .first()
        )