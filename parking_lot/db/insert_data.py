from sqlite3 import Error


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_slot(conn, slot):
    sql = ''' INSERT INTO parking_lot(slot_id,occupied)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, slot)
    conn.commit()
    return cur.lastrowid


def add_driver(conn, driver):
    sql = ''' INSERT INTO drivers(registration_number,driver_age)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, driver)
    conn.commit()
    return cur.lastrowid


def add_driver_slot(conn, driver_slot):
    sql = ''' INSERT INTO driver_slot(driver_id, slot_id)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, driver_slot)
    conn.commit()
    return cur.lastrowid


def update_slot_occupancy(conn, slot_id, o):
    print("update",slot_id,o)
    sql = ''' update  parking_lot set occupied=? where slot_id=?'''
    cur = conn.cursor()
    cur.execute(sql, (o, str(slot_id)))
    conn.commit()
