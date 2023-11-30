from sql_script import *


if __name__ == '__main__':

    connection, cursor = setup_db_connection()

    create_database(cursor, "cafe_management")

    create_database_tables(connection, cursor)   

    cursor.close()

    connection.close()
