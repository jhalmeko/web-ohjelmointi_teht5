from pymongo import MongoClient

import models_mongodb


class UsersMongodbRepository:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["sovelluskehykset_bad1"]
        self.collection = self.db["users"]
    def __del__(self):
        if self.client is not None:
            self.client.close()

    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute('SELECT * FROM users')
            result = cur.fetchall()
            users = []
            for user in result:
                users.append(models_mongodb.User(user[0], user[1], user[2], user[3]))

            return users