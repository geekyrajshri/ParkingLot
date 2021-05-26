def get_parking_slot(conn):
    sql = "SELECT slot_id FROM parking_lot where occupied=?"

    cur = conn.cursor()
    cur.execute(sql, (0,))

    rows = cur.fetchall()
    if len(rows) > 0:
        return rows[0]
    else:
        return None


def slots_for_driver_of_age(conn, age):
    sql = '''select slot_id from driver_slot where driver_id in (select id from drivers WHERE driver_age=?)'''

    cur = conn.cursor()
    cur.execute(sql, (age,))

    rows = cur.fetchall()
    res = ""
    if len(rows) > 0:
        for r in rows:
            res = res + str(r[0]) + ", "
        return res[0:len(res) - 2]
    else:
        return None


def slot_for_driver_with_registration_number(conn, registration_number):
    sql = 'select slot_id from driver_slot where driver_id = (select id from drivers WHERE registration_number=?)'
    cur = conn.cursor()
    cur.execute(sql, (registration_number,))
    rows = cur.fetchall()
    res = ""
    if len(rows) > 0:
        for r in rows:
            res = res + str(r[0])
        return res
    else:
        return None


def delete_driver_slot(conn, slot_id):
    sql = 'delete from driver_slot where slot_id =?'
    cur = conn.cursor()
    cur.execute(sql, (slot_id,))


def remove_driver_from_slot(conn, slot_id):
    sql = 'select driver_age, registration_number from drivers where id in (select driver_id from driver_slot WHERE slot_id=?)'
    cur = conn.cursor()
    cur.execute(sql, (slot_id,))
    rows = cur.fetchall()

    if len(rows) > 0:
        delete_driver_slot(conn, slot_id)
        return rows[0]
    else:
        return None


def vehicle_registration_number_for_driver_of_age(conn,driver_age):
    sql = 'select registration_number from drivers where driver_age=?'
    cur = conn.cursor()
    cur.execute(sql, (driver_age,))
    rows = cur.fetchall()

    res = ""
    if len(rows) > 0:
        for r in rows:
            res = res + str(r[0]) + ", "
        return res[0:len(res) - 2]
    else:
        return None
