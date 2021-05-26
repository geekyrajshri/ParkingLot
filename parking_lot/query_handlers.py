from parking_lot.db import connection, insert_data, query_data

DATABASE = r"parking_lot.db"


def get_connection():
    conn = connection.create_connection(DATABASE)
    return conn


def create_parking_lot(data):
    print(data)
    no_of_slots = data[1]
    conn = None
    try:
        conn = get_connection()
        for i in range(1, int(no_of_slots) + 1):
            slot = (i, 0)
            insert_data.create_slot(conn, slot)
        return f'Created parking of {no_of_slots} slots'
    except Exception as e:
        print(e.with_traceback())
    finally:
        if conn:
            conn.close()


def park_vehicle(data):
    print(data)
    registration_number = data[1]
    driver_age = int(data[3])
    conn = get_connection()
    slot_id = query_data.get_parking_slot(conn)
    if slot_id is not None:
        driver = (registration_number, driver_age)
        driver_id = insert_data.add_driver(conn, driver)
        driver_slot = (driver_id, slot_id)
        insert_data.add_driver_slot(conn, driver_slot)
        insert_data.update_slot_occupancy(conn, slot_id, '1')
        print(
            f'Car with vehicle registration number "{registration_number}" has been parked at slot number {"".join(slot_id)}')
        return f'Car with vehicle registration number "{registration_number}" has been parked at slot number {"".join(slot_id)}'
    else:
        print(f'No slots available')
        return f'No slots available'


def get_slot_numbers_for_driver_of_age(data):
    driver_age = data[1]
    conn = get_connection()
    slot_ids = query_data.slots_for_driver_of_age(conn, driver_age)
    if slot_ids is not None:
        print(slot_ids)
        return f'{slot_ids}'
    else:
        print(f'No slot found query')
        return f'No slot found query'


def get_slot_numbers_for_car_with_number(data):
    registration_number = data[1]
    conn = get_connection()
    slot_id = query_data.slot_for_driver_with_registration_number(conn, registration_number)
    if slot_id is not None:
        print(slot_id)
        return f'{slot_id}'
    else:
        print(f'No slot for car with {registration_number}')
        return f'No slot for car with {registration_number}'


def leave_parking_lot(data):
    slot_id = data[1]
    conn = get_connection()
    driver = query_data.remove_driver_from_slot(conn, slot_id)
    if driver is not None:
        insert_data.update_slot_occupancy(conn, slot_id, '0')
        print(
            f'Slot number {slot_id} vacated, the car with vehicle registration number "{driver["registration_number"]}" left the space, the driver of the car was of age {driver["age"]}')
        return f'Slot number {slot_id} vacated, the car with vehicle registration number "{driver["registration_number"]}" left the space, the driver of the car was of age {driver["age"]}'
    else:
        print(f'Slot already vacant')
        return f'Slot already vacant'


def get_vehicle_registration_number_for_driver_of_age(data):
    driver_age = data[1]
    conn = get_connection()
    registration_numbers = query_data.vehicle_registration_number_for_driver_of_age(conn, driver_age)
    if registration_numbers is not None:
        print(registration_numbers)
        return f'{registration_numbers}'
    else:
        print(f'No parked car matches the query')
        return f'No parked car matches the query'
