from flask import jsonify

from decorators.db_conn import get_db_conn
from decorators.repository_decorator import init_repository
from models_mysql import User
from repositories.repository_factory import users_repository_factory
from repositories.users_mysql_repository import UsersMysqlRepository
from repositories.users_postgres_repository import UsersPostgressRepository
from repositories.users_mongodb_repository import UsersMongodbRepository


# Nyt jokaista controlleria vastaa yksi tiedosto. Tiedostot sisältävät kaikki funktiot,jotka pitävät
# huolen requestin vastaanottamisesta ja responsen lähettämisestä.

@get_db_conn
@init_repository('users_repo')
def get_all_users(repo):

    users =  repo.get_all()
    users_json = []
    for user in users:
        users_json.append({
            'id': user.id,
            'username': user.username,
            'firstname': user.firstname,
            'lastname': user.lastname,
        })
    return jsonify(users_json)