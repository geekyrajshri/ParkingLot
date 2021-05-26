def get_parking_slot(conn):
    sql = ''' SELECT slot_id FROM parking_lot where occupied="0"'''

    cur = conn.cursor()
    cur.execute(sql)

    rows = cur.fetchall()
    print(rows)
    if len(rows) > 0:
        return ''.join(rows[0])
    else:
        return None


def slots_for_driver_of_age(conn, age):
    sql = '''select slot_id from driver_slot where driver_id in ("select id from drivers WHERE driver_age=?")'''

    cur = conn.cursor()
    cur.execute(sql, (age,))

    rows = cur.fetchall()

    if len(rows) > 0:
        return list(rows)
    else:
        return None


def slot_for_driver_with_registration_number(conn, regitration_number):
    sql = 'select slot_id from driver_slot where driver_id = ("select id from drivers WHERE registration_number=?")'

    cur = conn.cursor()
    cur.execute(sql, (regitration_number,))

    rows = cur.fetchall()

    if len(rows) > 0:
        return str(rows[0])
    else:
        return None


def delete_driver_slot(conn, slot_id):
    sql = 'delete from driver_slot where slot_id =?")'
    cur = conn.cursor()
    cur.execute(sql, (slot_id,))


def remove_driver_from_slot(conn, slot_id):
    sql = 'select id,registration_number  from drivers where id = ("select driver_id from driver_slot WHERE slot_id=?")'

    cur = conn.cursor()
    cur.execute(sql, (slot_id,))
    rows = cur.fetchall()
    if len(rows) > 0:
        delete_driver_slot(conn, slot_id)
        return str(rows[0])
    else:
        return None


def get_vehicle_registration_number_for_driver_of_age():
    pass
