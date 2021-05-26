from parking_lot import setup_db
from parking_lot.query_handlers import create_parking_lot, park_vehicle, get_slot_numbers_for_driver_of_age, \
    get_slot_numbers_for_car_with_number, get_vehicle_registration_number_for_driver_of_age, leave_parking_lot

INPUT_FILE = 'parking_lot/data/input.txt'
OUTPUT_FILE = 'parking_lot/data/output.txt'


def read_data(filename=INPUT_FILE):
    file = open(filename, "r")
    parking_queries = file.read()
    file.close()
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
    response = handle(data)
    return response


def execute_parking_queries(parking_queries):
    try:
        tasks = parking_queries.splitlines()
        responses = []
        for task in tasks:
            details = task.split(" ")
            handler = detect_query(details)
            responses.append(execute_query(handler["handle"], handler["data"]))
        return responses
    except Exception as e:
        print(e.with_traceback())


def update_response(responses):
    file = open(OUTPUT_FILE, "w")

    for response in responses:
        file.write(response + "\n")
    file.close()


def database_setup():
    setup_db.database_setup()


def run():
    database_setup()
    parking_queries = read_data()
    responses = execute_parking_queries(parking_queries)
    update_response(responses)
