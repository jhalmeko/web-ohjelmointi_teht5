from pymongo import MongoClient

class User:
    def __init__(self, _id, username, firstname, lastname):
        self.id = _id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def get_all(cls):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["sovelluskehykset_bad1"]
        collection = db["users"]
        result = collection.find()
        users = []
        for user in result:
            users.append(cls(user[0], user[1], user[2], user[3]))
        client.close()

        return users
    


class Product:
    def __init__(self, _id, productname, productprice):
        self.id = _id
        self.productname = productname
        self.productprice = productprice

    @classmethod
    def get_all(cls):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["sovelluskehykset_bad1"]
        collection = db["products"]
        result = collection.find()
        products = []
        for product in result:
            products.append(cls(product[0], product[1], product[2]))
        client.close()

        return products
    


class Vehicle:
    def __init__(self, _id, vehiclename, vehicleprice):
        self.id = _id
        self.vehiclename = vehiclename
        self.vehicleprice = vehicleprice

    @classmethod
    def get_all(cls):
        client = MongoClient("mongodb://localhost:27017/")
        db = client["sovelluskehykset_bad1"]
        collection = db["vehicles"]
        result = collection.find()
        vehicles = []
        for vehicle in result:
            vehicles.append(cls(vehicle[0], vehicle[1], vehicle[2]))
        client.close()

        return vehicles