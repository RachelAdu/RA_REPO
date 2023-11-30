import pymysql
import os
from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")

def setup_db_connection(host=host_name, 
                        user=user_name, 
                        password=user_password):

    connection = pymysql.connect(
        host = host,
        user = user,
        password = password
    )
    
    cursor = connection.cursor()
    return connection, cursor

def create_database(cursor, db_name):
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
    cursor.execute(f"USE {db_name};")

def create_database_tables(connection, cursor):

    create_couriers_table = \
    """
        CREATE TABLE IF NOT EXISTS couriers (
            courier_id VARCHAR(50) NOT NULL, AUTO INCREMENT
            courier_name VARCHAR(50),
            courier_number INT(11),
            PRIMARY KEY (courier_id)
        );
    """
    
    create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
            product_id VARCHAR(50) NOT NULL, AUTO INCREMENT
            product_name VARCHAR(50),
            prooduct_price DECIMAL(10,2),
            PRIMARY KEY (product_id)
        );
    """

    cursor.execute(create_couriers_table)
    cursor.execute(create_products_table)
    connection.commit()