from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, event, update, delete
from datetime import date
from danskcargo_data import Container, Aircraft, Transport, Base
from sqlalchemy.engine import Engine

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


Database = 'sqlite:///danskcargo.db'

# region test data
def create_test_data():
    with Session(engine) as session:
        new_items = [
            Container(weight=1200, destination="Oslo"),
            Container(weight=700, destination="Helsinki"),
            Container(weight=1800, destination="Helsinki"),
            Container(weight=1000, destination="Helsinki"),
            Aircraft(max_cargo_weight=2000, registration="OY-CBS"),
            Aircraft(max_cargo_weight=3000, registration="OY-THR"),
            Transport(date=date(2022, 12, 10), container_id=2, aircraft_id=1)
        ]
        session.add_all(new_items)
        session.commit()


def reset_data():
    delete_all(Transport)
    delete_all(Container)
    delete_all(Aircraft)
    create_test_data()


def delete_all(class_):
    with Session(engine) as session:
        for record in select_all(class_):
            session.execute(delete(class_).where(class_.id == record.id))
        session.commit()
# endregion


def select_all(classparam):
    with Session(engine) as session:
        records = session.scalars(select(classparam))
        result = []
        for record in records:
            print(record)
            result.append(record)
    return result


def get_record(classparam, record_id):
    with Session(engine) as session:
        record = session.scalars(select(classparam).where(classparam.id == record_id)).first()
    return record


def create_record(record):
    with Session(engine) as session:
        record.id = None
        session.add(record)
        session.commit()


# region Container
def update_container(container):
    with Session(engine) as session:
        session.execute(update(Container).where(Container.id == container.id). values(weight=container.weight, destination=container.destination))
        session.commit()


def delete_hard_container(container):
    with Session(engine) as session:
        session.execute(delete(Container).where(Container.id == container.id))
        session.commit()


def delete_soft_container(container):
    with Session(engine) as session:
        session.execute(update(Container).where(Container.id == container.id).values(weight=-1, destination=container.destination))
        session.commit()
# endregion

# region Aircraft
def update_aircraft(aircraft):
    with Session(engine) as session:
        session.execute(update(Aircraft).where(Aircraft.id == aircraft.id).values(max_cargo_weight=aircraft.max_cargo_weight, registration=aircraft.registration))
        session.commit()


def delete_hard_aircraft(aircraft):
    with Session(engine) as session:
        session.execute(delete(Aircraft).where(Aircraft.id == aircraft.id))
        session.commit()


def delete_soft_aircraft(aircraft):
    with Session(engine) as session:
        session.execute(update(Aircraft).where(Aircraft.id == aircraft.id).values(max_cargo_weight=-1, registration=aircraft.registration))
        session.commit()
# endregion

# region Transport
def update_transport(transport):
    with Session(engine) as session:
        session.execute(update(Transport).where(Transport.id == transport.id).values(date=transport.date, container_id=transport.container_id, aircraft_id=transport.aircraft_id))
        session.commit()


def delete_hard_transport(transport):
    with Session(engine) as session:
        session.execute(delete(Transport).where(Transport.id == transport.id))
        session.commit()
# endregion


if __name__ == "__main__":
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
    reset_data()
    print('\n', select_all(Container))
    print('\n', select_all(Aircraft))
    print('\n', select_all(Transport))
    print('\n', get_record(Container, 4))
    print('\n', get_record(Aircraft, 2))
    print('\n', get_record(Transport, 1))
else:
    engine = create_engine(Database, echo=False, future=True)
    Base.metadata.create_all(engine)
