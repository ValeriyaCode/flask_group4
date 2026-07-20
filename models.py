from peewee import *

db = SqliteDatabase('db.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class Company(BaseModel):
    id = PrimaryKeyField()
    name = CharField(unique=True)
    password = CharField()


class Product(BaseModel):
    name = CharField(unique=True)
    price = FloatField()
    category = CharField()

    # кожен товар прив'язаний до компанії
    company = ForeignKeyField(Company, backref='products')


def init_db():
    db.connect()
    # db.drop_tables([Company, Product])
    db.create_tables([Company, Product])

