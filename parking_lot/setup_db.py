import os

from parking_lot.db import connection, insert_data

DATABASE = r"parking_lot.db"


def database_setup():
    os.remove(DATABASE)
    sql_create_drivers_table = """ CREATE TABLE IF NOT EXISTS drivers (
                                            id integer PRIMARY KEY,
                                            registration_number VARCHAR(255),
                                            driver_age INT
                                        ); """

    sql_create_parking_lot_table = """CREATE TABLE IF NOT EXISTS parking_lot (
                                            slot_id integer PRIMARY KEY,
                                            occupied INT
                                        );"""

    sql_create_driver_parking_slot_table = """CREATE TABLE IF NOT EXISTS driver_slot (
                                            id integer PRIMARY KEY,
                                            driver_id   INTEGER NOT NULL,
                                            slot_id INTEGER NOT NULL,
                                            FOREIGN KEY (driver_id) REFERENCES users (id),
                                            FOREIGN KEY (slot_id) REFERENCES parking_lot (slot_id)
                                        );"""

    # create a database connection
    conn = connection.create_connection(DATABASE)

    # create tables
    if conn is not None:
        # create drivers table
        insert_data.create_table(conn, sql_create_drivers_table)

        # create parking_lot table
        insert_data.create_table(conn, sql_create_parking_lot_table)

        # create driver_slot table
        insert_data.create_table(conn, sql_create_driver_parking_slot_table)

    else:
        print("Error! cannot setup database connection.")
