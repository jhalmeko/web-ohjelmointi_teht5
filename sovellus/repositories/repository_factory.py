import os

from repositories.users_postgres_repository import UsersPostgressRepository
from repositories.users_mysql_repository import UsersMysqlRepository
from repositories.users_mongodb_repository import UsersMongodbRepository


def users_repository_factory(con):
    _db = os.getenv('DB')
    repo = None
    if _db == 'mysql':
        repo = UsersMysqlRepository()
    elif _db == 'postgres':
        repo = UsersPostgressRepository()
    elif _db == 'mongodb':
        repo = UsersMongodbRepository()
    else:
        repo = UsersMysqlRepository()