def main():
    database = r"parking_lot.db"

    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        registration_number VARCHAR(255),
                                        age INT
                                    ); """

    sql_create_parking_lot_table = """CREATE TABLE IF NOT EXISTS parking_lot (
                                        slot_id integer PRIMARY KEY,
                                        occupied VARCHAR(25)
                                    );"""

    sql_create_user_parking_slot_table = """CREATE TABLE IF NOT EXISTS user_slot (
                                        id integer PRIMARY KEY,
                                        user_id   INTEGER NOT NULL,
                                        slot_id INTEGER NOT NULL,
                                        FOREIGN KEY (user_id) REFERENCES users (id),
                                        FOREIGN KEY (slot_id) REFERENCES parking_lot (slot_id)
                                    );"""

    # create a database connection
    # conn = create_connection(database)

    # create tables
    # if conn is not None:
        # create users table
        # create_table(conn, sql_create_users_table)

        # create parking_lot table
        # create_table(conn, sql_create_parking_lot_table)

        # create user_slot table
        # create_table(conn, sql_create_user_parking_slot_table)

        # with conn:
            # create a new Parking Lot
            # slot = (1, 0);
            # create_slot(conn, slot);

            # cur = conn.cursor()
            # cur.execute("SELECT * FROM parking_lot")
            #
            # rows = cur.fetchall()
            #
            # for row in rows:
            #     print(row)

            # Add New User
            # user = ('KA-01-HH-1234', '21')

            # add_user(conn, user)
            # cur = conn.cursor()
            # cur.execute("SELECT * FROM users")
            #
            # rows = cur.fetchall()
            #
            # for row in rows:
            #     print(row)

            # Allot slot to user
            # user_slot = (1, 1)
            # add_user_slot(conn, user_slot)

            # cur = conn.cursor()
            # cur.execute("SELECT * FROM user_slot")
            #
            # rows = cur.fetchall()
            #
            # for row in rows:
            #     print(row)

    # create_task(conn, task_2)
    # else:
    #     print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
