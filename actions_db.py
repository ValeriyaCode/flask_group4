from models import Product, Company

'''Companies'''

def add_company(name: str, password: str):
    Company.create(name=name, password=password)

def company_exist(name: str) -> bool:
    return Company.select().where(Company.name == name).exists()

def get_company_by_name(name: str) -> Company:
    return Company.get_or_none(name=name)

'''Products'''

def add_product(name: str, price: float, category: str):
    Product.create(name=name, price=price, category=category)

def get_categories():
    products = Product.select(Product.category).distinct().order_by(Product.category)
    categories = [product.category for product in products]
    return categories

def get_products():
    return Product.select()

def get_products_by_category(category: str):
    return Product.select().where(Product.category == category)

def product_exists(name: str) -> bool:
    return Product.select().where(Product.name == name).exists()

def edit_product():
    pass

def delete_product():
    pass

