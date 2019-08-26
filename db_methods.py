import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'data.sqlite3')


def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


db_connect()

from db_utils import db_connect
con = db_connect() # connect to the database
cur = con.cursor() # instantiate a cursor obj
customers_sql = """
CREATE TABLE customers (
     id integer PRIMARY KEY,
     first_name text NOT NULL,
     last_name text NOT NULL)"""
cur.execute(customers_sql)
products_sql = """
 CREATE TABLE products (
     id integer PRIMARY KEY,
     name text NOT NULL,
     price real NOT NULL)"""
cur.execute(products_sql)


