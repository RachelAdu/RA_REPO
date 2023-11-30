import pymysql
import os
from menu_functions import load_data
from tabulate import tabulate

from dotenv import load_dotenv

load_dotenv()
host_name = os.environ.get("mysql_host")
database_name = os.environ.get("mysql_db")
user_name = os.environ.get("mysql_user")
user_password = os.environ.get("mysql_pass")



def database_c_add(name, number):
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
    ) as connection:
        # cursor connection
        cursor = connection.cursor()
        sql = """
                INSERT INTO `couriers` (courier_name, courier_contact_number)
                VALUES (%s, %s)
                """
        data_values = ({name},{number})
        cursor.execute(sql, data_values)
        connection.commit()
        cursor.close()
        print('New courier added!')

def dbc_remove():
    remove_c = int(input("Enter the number associated with the courier that you would you like to remove? "))
    with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
    ) as connection:
        cursor = connection.cursor()
        sql = """
                DELETE FROM couriers WHERE courier_id = %s
                """
        data_values = ({remove_c})
        cursor.execute(sql, data_values)
        connection.commit()
        cursor.close()
        print("Courier has been removed")
    
# FUNCTIONS
def database_c():
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
    ) as connection:
        print('\nList of Couriers available:')
    # cursor connection
        cursor = connection.cursor()
    # retrieving info
        cursor.execute('SELECT* FROM couriers')
        rows = cursor.fetchall()
        print(tabulate(rows, headers=['Courier ID', 'Courier Name', 'Courier Contact Number'], tablefmt='psql'))
        cursor.close()


def database_c_update(name, position):
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
    ) as connection:
        cursor = connection.cursor()
        sql = """
                UPDATE couriers SET courier_name = %s WHERE courier_id = %s
                """
        data_values = ({name}, {position})
        cursor.execute(sql, data_values)
        connection.commit()
        cursor.close()
        print('Courier updated successfully')

def dbc_update_num(number, position):
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
    ) as connection:
        cursor = connection.cursor()
        sql = """
                UPDATE couriers SET courier_number = %s WHERE courier_id = %s
                """
        data_values = ({number}, {position})
        cursor.execute(sql, data_values)
        connection.commit()
        cursor.close()
        print('Courier updated successfully')

def database_p():
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
    ) as connection:
        print('\nList of Products available:')
    # cursor connection
        cursor = connection.cursor()
    # retrieving info
        cursor.execute('SELECT* FROM products')
        rows = cursor.fetchall()
        print(tabulate(rows, headers=['Product ID', 'Product Name', 'Product Price'], tablefmt='psql'))
        cursor.close()
    # displaying info    
        # for row in rows:
        #     print(f'Product ID: {row[0]}, Product Name: {row[1]}, Product Price: {row[2]}')
        #print("These are the couriers available")

def db_p_add(name, price):
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
    ) as connection:
        cursor = connection.cursor()
        sql = """
                INSERT INTO `products` (product_name, product_price)
                VALUES (%s, %s)
                """
        data_values = ({name},{price})
        cursor.execute(sql, data_values)
        connection.commit()
        cursor.close()
        print('New product added!')

def dbp_update_name(name, position):
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
    ) as connection:
        cursor = connection.cursor()
        sql = """
                UPDATE products SET product_name = %s WHERE product_id = %s
                """
        data_values = ({name}, {position})
        cursor.execute(sql, data_values)
        connection.commit()
        cursor.close()

def dbp_update_price(price, position):
    with pymysql.connect(
        host = host_name, database = database_name,
        user = user_name, password = user_password
    ) as connection:
        cursor = connection.cursor()
        sql = """
                UPDATE products SET product_price = %s WHERE product_id = %s
                """
        data_values = ({price}, {position})
        cursor.execute(sql, data_values)
        connection.commit()
        cursor.close()

def dbp_remove():
    not_want = int(input("Enter the number associated with the item that you would you like to remove? "))
    with pymysql.connect(
            host = host_name, database = database_name,
            user = user_name, password = user_password
    ) as connection:
        cursor = connection.cursor()
        sql = """
                DELETE FROM products WHERE product_id = %s
                """
        data_values = ({not_want})
        cursor.execute(sql, data_values)
        connection.commit()
        cursor.close()
        print("Product has been removed")