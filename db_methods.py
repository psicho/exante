import os
import sqlite3
import time

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'data.sqlite3')


def connect_db(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con


def commit_and_close_db(con):
    con.commit()
    con.close()


def create_tables(db_path=DEFAULT_PATH):
    con = connect_db()

    # Create table commodity
    con.execute('''CREATE TABLE commodity (
                        product text,
                        exchange text,
                        combined_commodity text)''')

    # Create table risk_arrays
    con.execute('''CREATE TABLE risk_arrays (
                        created timestamp without time zone NOT NULL, 
                        product text, 
                        exchange text,
                        product_type text,
                        contract_month date,
                        strike_price numeric,
                        option_right text,
                        risk_array numeric[],
                        delta numeric,
                        implied_volatility numeric,
                        settlement_price numeric)''')

    # Save (commit) the changes
    con.commit()

    # close connection database
    con.close()


def add_row_to_data_base(table_for_add, *args):
    con = connect_db()
    # print(args)
    sd = str(args).strip('()')
    # Insert a row of data
    con.execute("INSERT INTO %s VALUES (%s)" %(table_for_add, sd))

    # Save (commit) the changes
    con.commit()

    # close connection database
    con.close()


def add_commodity_to_data_base(product, exchange, combined_commodity):
    pass


# create_tables()
add_row_to_data_base('commodity', 'product', 'exchange', 'combined_commodity')
add_row_to_data_base('risk_arrays', '32398r238r2', 'product', 'exchange', 'product_type', '2019-08-28', 20156, 'option_right', '(123,334,334)', 223, 444, 666)











# conn = sqlite3.connect('example.db')



# db_connect()

# from db_utils import db_connect
# con = db_connect() # connect to the database
# cur = con.cursor() # instantiate a cursor obj
# customers_sql = """
# CREATE TABLE customers (
#      id integer PRIMARY KEY,
#      first_name text NOT NULL,
#      last_name text NOT NULL)"""
# cur.execute(customers_sql)
# products_sql = """
#  CREATE TABLE products (
#      id integer PRIMARY KEY,
#      name text NOT NULL,
#      price real NOT NULL)"""
# cur.execute(products_sql)


