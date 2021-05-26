import parking_lot.setup_db as sdb
from parking_lot.db import connection, insert_data, query_data


def get_connection(db):
    conn = connection.create_connection(db)
    return conn


def create_parking_lot(data, db=sdb.DATABASE):
    no_of_slots = data[1]
    conn = None
    try:
        conn = get_connection(db)
        for i in range(1, int(no_of_slots) + 1):
            slot = (i, 0)
            insert_data.create_slot(conn, slot)
        print(f'Created parking of {no_of_slots} slots')
        return f'Created parking of {no_of_slots} slots'
    except Exception as e:
        print(e.with_traceback())
    finally:
        if conn:
            conn.close()


def park_vehicle(data, db=sdb.DATABASE):
    registration_number = data[1]
    driver_age = int(data[3])
    conn = get_connection(db)
    slot_id = query_data.get_parking_slot(conn)
    if slot_id is not None:
        driver = (registration_number, driver_age)
        driver_id = insert_data.add_driver(conn, driver)
        driver_slot = (driver_id, slot_id[0])
        insert_data.add_driver_slot(conn, driver_slot)
        insert_data.update_slot_occupancy(conn, int(slot_id[0]), 1)
        conn.close()
        print(
            f'Car with vehicle registration number "{registration_number}" has been parked at slot number {str(slot_id[0])}')
        return f'Car with vehicle registration number "{registration_number}" has been parked at slot number {str(slot_id[0])}'
    else:
        print(f'No slots available')
        return f'No slots available'


def get_slot_numbers_for_driver_of_age(data, db=sdb.DATABASE):
    driver_age = data[1]
    conn = get_connection(db)
    slot_ids = query_data.slots_for_driver_of_age(conn, int(driver_age))
    if slot_ids is not None:
        print(slot_ids)
        return f'{slot_ids}'
    else:
        print(f'No parked car matches the query')
        return f'No parked car matches the query'


def get_slot_numbers_for_car_with_number(data, db=sdb.DATABASE):
    registration_number = data[1]
    conn = get_connection(db)
    slot_id = query_data.slot_for_driver_with_registration_number(conn, registration_number)
    if slot_id is not None:
        print(slot_id)
        return f'{slot_id}'
    else:
        print(f'No parked car matches the query')
        return f'No parked car matches the query'


def leave_parking_lot(data, db=sdb.DATABASE):
    slot_id = data[1]
    conn = get_connection(db)
    driver = query_data.remove_driver_from_slot(conn, int(slot_id))
    if driver is not None:
        insert_data.update_slot_occupancy(conn, slot_id, 0)
        print(
            f'Slot number {slot_id} vacated, the car with vehicle registration number "{driver[1]}" left the space, the driver of the car was of age {driver[0]}')
        return f'Slot number {slot_id} vacated, the car with vehicle registration number "{driver[1]}" left the space, the driver of the car was of age {driver[0]}'
    else:
        print(f'Slot already vacant')
        return f'Slot already vacant'


def get_vehicle_registration_number_for_driver_of_age(data, db=sdb.DATABASE):
    driver_age = data[1]
    conn = get_connection(db)
    registration_numbers = query_data.vehicle_registration_number_for_driver_of_age(conn, driver_age)
    if registration_numbers is not None:
        print(registration_numbers)
        return f'{registration_numbers}'
    else:
        print(f'No parked car matches the query')
        return f'No parked car matches the query'
