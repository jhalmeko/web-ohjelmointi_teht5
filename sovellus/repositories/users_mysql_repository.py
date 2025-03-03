import mysql.connector

import models_mysql


class UsersMysqlRepository:
    def __init__(self):
        self.con = mysql.connector.connect(user='root', database='sovelluskehykset_bad1')


    def __del__(self):
        if self.con is not None and self.con.is_connected():
            self.con.close()

    def get_all(self):
        with self.con.cursor() as cur:
            cur.execute('SELECT * FROM users')
            result = cur.fetchall()
            users = []
            for user in result:
                users.append(models_mysql.User(user[0], user[1], user[2], user[3]))

            return users