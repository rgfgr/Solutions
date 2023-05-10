"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Anvend det, du har lært i dette kapitel om databaser, på en første opgave.

Trin 1:
Opret en ny SQLite database "S2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import create_engine, select

Database = 'sqlite:///S2311_my_second_sql_database.db'
Base = declarative_base()


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f"Customer({self.id=} {self.name=} {self.address=} {self.age=})"


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Float)
    brand = Column(String)

    def __repr__(self):
        return f"Product({self.id=} {self.product_number=} {self.price=} {self.brand=})"


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            result.append(record)
    return result


def get_record(classparam, record_id):
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


def create_test_data():
    with Session(engine) as session:
        new_items = [
            Customer(name="peter", address="fuckoff", age=123),
            Customer(name="susan", address="fuckoff", age=53),
            Customer(name="jane", address="fuckoff", age=12),
            Customer(name="harry", address="harry mc harry street", age=44),
            Product(product_number=1234, price=15.5, brand="no"),
            Product(product_number=53, price=1.5, brand="adw"),
            Product(product_number=64, price=88.4, brand="ge"),
            Product(product_number=75, price=34.53, brand="hrt"),
        ]
        session.add_all(new_items)
        session.commit()


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

# create_test_data()
print()
print(select_all(Customer), '\n')
print(select_all(Product), '\n')
for i in range(1, len(select_all(Customer)) + 1):
    print(get_record(Customer, i))
print()
for i in range(1, len(select_all(Product)) + 1):
    print(get_record(Product, i))
