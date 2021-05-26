from parking_lot import setup_db
from parking_lot.query_handlers import create_parking_lot, park_vehicle, get_slot_numbers_for_driver_of_age, \
    get_slot_numbers_for_car_with_number, get_vehicle_registration_number_for_driver_of_age, leave_parking_lot

INPUT_FILE = 'parking_lot/data/input.txt'


def read_data():
    file = open(INPUT_FILE, "r")
    parking_queries = file.read()
    return parking_queries


def get_query_handler(details):
    parking_lot_operation = {
        "Create_parking_lot": {"handle": create_parking_lot, "data": details},
        "Park": {"handle": park_vehicle, "data": details},
        "Slot_numbers_for_driver_of_age": {"handle": get_slot_numbers_for_driver_of_age, "data": details},
        "Slot_number_for_car_with_number": {"handle": get_slot_numbers_for_car_with_number, "data": details},
        "Leave": {"handle": leave_parking_lot, "data": details},
        "Vehicle_registration_number_for_driver_of_age": {"handle": get_vehicle_registration_number_for_driver_of_age,
                                                          "data": details}
    }

    return parking_lot_operation[details[0]]


def detect_query(details):
    try:
        handler = get_query_handler(details)
        return handler
    except Exception as e:
        print(e)


def execute_query(handle, data):
    handle(data)


def execute_parking_queries(parking_queries):
    try:
        tasks = parking_queries.splitlines()
        for task in tasks:
            details = task.split(" ")
            handler = detect_query(details)
            execute_query(handler["handle"], handler["data"])
    except Exception as e:
        print(e.with_traceback())


def run():
    setup_db.database_setup()
    parking_queries = read_data()
    execute_parking_queries(parking_queries)
