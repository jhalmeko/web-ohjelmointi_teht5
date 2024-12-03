import contextlib
import os
import mysql.connector
import psycopg2
from pymongo import MongoClient


@contextlib.contextmanager
def init_db_conn():
    conn = None
    try:
        _db = os.getenv('DB')
        if _db == 'mysql':
            conn = mysql.connector.connect(user="root", database="sovelluskehykset_bad1", password="code1819")

        elif _db == 'postgres':
            conn = psycopg2.connect(user="postgres", database="sovelluskehykset_bad1", password="code1819")
        elif _db == 'mongodb':
            conn = MongoClient.connector.connect(user="mongodb", database="sovelluskehykset_bad1", password="code1819")
        yield conn
    finally:
        if conn is not None:
            conn.close()