from app.models.brands import Brand
from app.repositories.brand_repository import BrandRepository
from app.schemas.brand import BrandCreate

class BrandService():
    def __init__(self,repo: BrandRepository):
        self.repo = repo
    
    def create_brand(self,brand : BrandCreate):
        exits_brand = self.repo.get_by_name(brand.name)
        if exits_brand:
            raise ValueError(f"La marca con el nombre {brand.name} ya esta registrada")
        new_brand = Brand(
            name = brand.name
        )
        return self.repo.create(new_brand)
    
    def get_all(self):
        return self.repo.get_all()
    