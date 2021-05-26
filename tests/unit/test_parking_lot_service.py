import os
from unittest import mock
from unittest.mock import Mock

from parking_lot import parking_lot_service, setup_db


@mock.patch("parking_lot.parking_lot_service.database_setup")
@mock.patch("parking_lot.parking_lot_service.read_data", )
@mock.patch("parking_lot.parking_lot_service.execute_parking_queries")
def test_should_execute_run_function_call_parking_lot_methods(mocked_execute_queries, mocked_read_data,
                                                              mocked_database_setup):
    parking_lot_service.run()
    mocked_database_setup.return_value = Mock()
    mocked_read_data.return_value = Mock()
    mocked_execute_queries.return_value = Mock()
    mocked_database_setup.assert_called()
    mocked_execute_queries.assert_called()
    mocked_read_data.assert_called()


def test_should_successfully_read_data_input_file():
    filename = 'test_data.txt'
    try:
        expected_data: str = 'Create Parking Lot of size 3'
        file = open(filename, "w")
        file.write(expected_data)
        file.close()
        actual_data = parking_lot_service.read_data(filename)
        assert actual_data == expected_data
    finally:
        file.close()
        os.remove(filename)


def test_should_successfully_execute_query():
    query: str = 'Create_parking_lot 1\n'
    setup_db.database_setup(r'test.db')

    actual_data = parking_lot_service.execute_parking_queries(query, r'test.db')
    assert actual_data == ['Created parking of 1 slots']

