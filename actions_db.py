from models import Product, Company

'''Companies'''

def add_company(name: str, password: str):
    Company.create(name=name, password=password)

def company_exist(name: str) -> bool:
    return Company.select().where(Company.name == name).exists()

def get_company_by_name(name: str) -> Company:
    return Company.get_or_none(name=name)


'''Products'''

def add_product(name: str, price: float, category: str, company_id: int):
    Product.create(name=name, price=price, category=category, company=company_id)

def get_categories(company_id: int):
    products = Product.select(Product.category).where(Product.company == company_id).distinct().order_by(Product.category)
    categories = [product.category for product in products]
    return categories

def get_products(company_id: int):
    return Product.select().where(Product.company == company_id)

def get_products_by_category(category: str, company_id: int):
    return Product.select().where((Product.category == category) & (Product.company == company_id))

def product_exists(name: str, company_id: int) -> bool:
    return Product.select().where((Product.name == name) & (Product.company == company_id)).exists()

def edit_product(name: str, new_price: float, new_category: str, company_id: int):
    (
        Product
        .update(price=new_price, category=new_category)
        .where((Product.name == name) & (Product.company == company_id)).execute()
     )

def delete_product(name: str, company_id: int):
    Product.delete().where((Product.name == name) & (Product.company == company_id)).execute()

