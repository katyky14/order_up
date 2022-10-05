from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)


    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")
    db.session.add(beverages)
    db.session.add(entrees)
    db.session.add(sides)


    dinner = Menu(name="Dinner")
    db.session.add(dinner)

    fries = MenuItem(name="French fries", price=3.50, menu_type_id=3, menu_id=1)
    drp = MenuItem(name="Dr. Pepper", price=1.0, menu_type_id=1, menu_id=1)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, menu_type_id=2, menu_id=1)
    db.session.add(fries)
    db.session.add(drp)
    db.session.add(jambalaya)

    table1 = Table(number=1, capacity=4)
    table2 = Table(number=2, capacity=4)
    table3 = Table(number=3, capacity=4)
    table4 = Table(number=4, capacity=4)
    table5 = Table(number=5, capacity=4)
    table6 = Table(number=6, capacity=4)
    table7 = Table(number=7, capacity=4)
    table8 = Table(number=8, capacity=4)
    table9 = Table(number=9, capacity=4)
    table10 = Table(number=10, capacity=4)

    tables = [table1, table2, table3, table4, table5, table6, table7, table8, table9, table10]

    for table in tables:
        db.session.add(table)


    db.session.commit()
