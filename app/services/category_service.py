from app.models.categories import Category
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate

class CategoryService():
    def __init__(self, repo : CategoryRepository):
       self.repo = repo
    
    def create_category(self, category :CategoryCreate):
        category_exixts = self.repo.get_by_name(category.name)
        if category_exixts:
            raise ValueError(f"La categoria con nombre {category.name} ya esta registrada")
        
        new_category = Category(
            name= category.name
        )
        return self.repo.create(new_category)
    
    def get_all(self):
        return self.repo.get_all()