import psycopg2


class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def get_all(cls):
        with psycopg2.connect(user='root', database='sovelluskehykset_bad1') as con:
            with con.cursor() as cur:
                cur.execute('SELECT * FROM users')
                result = cur.fetchall()
                users = []
                for user in result:
                    users.append(cls(user[0], user[1], user[2], user[3]))

                return users
            

class Product:
    def __init__(self, _id, productname, productprice):
        self.id = _id
        self.productname = productname
        self.productprice = productprice

    @classmethod
    def get_all(cls):
        with psycopg2.connect(product='root', database='sovelluskehykset_bad1') as con:
            with con.cursor() as cur:
                cur.execute('SELECT * FROM products')
                result = cur.fetchall()
                products = []
                for product in result:
                    products.append(cls(product[0], product[1], product[2]))

                return products
            

class Vehicle:
    def __init__(self, _id, vehiclename, vehicleprice):
        self.id = _id
        self.vehiclename = vehiclename
        self.vehicleprice = vehicleprice

    @classmethod
    def get_all(cls):
        with psycopg2.connect(vehicle='root', database='sovelluskehykset_bad1') as con:
            with con.cursor() as cur:
                cur.execute('SELECT * FROM vehicles')
                result = cur.fetchall()
                vehicles = []
                for vehicle in result:
                    vehicles.append(cls(vehicle[0], vehicle[1], vehicle[2]))

                return vehicles