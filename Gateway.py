from flask import Flask
import logging
from Executor import TestExecutor

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)


executor = TestExecutor()


@app.route("/test_file/<file_name>", methods=['GET'])
def execute_file(file_name):
    """
    Receiving GET request that contains the test file name.
    The component called TestExecutor will find the file, execute the test and pass the test execution
    report back to this method. The report will be returned to the customer.
    If the file can't be found relevant error message will be returned.
    """

    if "." not in file_name:
        return {"error": "File extension must PY"}

    file_extension = file_name.split('.')[1]

    # Verifying given file is a Python file
    if file_extension != "py":
        return {"error": "File extension must PY"}

    logging.info(f'Gateway: Received a request to run all tests in file {file_name}')

    # File name is sent to TestExecutor component. Expecting execution report in JSON, that will be returned.
    return executor.run_test_file(file_name)


@app.route("/test_folder/<folder_name>", methods=['GET'])
def execute_all_in_folder(folder_name):
    """
    Receiving GET request that contains the test folder name.
    The component called TestExecutor will find the folder, execute all the tests in all files in it
    and pass the test execution report back to this method. The report will be returned to the customer.
    :param folder_name: the name of the folder that contains the test files that are to be executed
    """

    logging.info(f'Gateway: Received a request to run all tests in all files that the folder {folder_name} contains')

    # Folder name will be sent to TestExecutor component. Expecting execution report in JSON, that will be returned.
    return executor.run_test_folder(folder_name)

@app.route("/tests_marked/<test_marker>", methods=['GET'])
def execute_tests_by_mark(test_marker):
    """
    Receiving GET request that contains a test marker (String) - must be one of the existing test marks
    defined in pytest.ini. All the tests with given marker will be executed
    :param test_marker: all tests with that mark will be executed
    """

    logging.info(f'Gateway: Received a request to run all tests marked with the following marker -  {test_marker}')

    # Required mark will be sent to TestExecutor component. Expecting execution report in JSON, that will be returned.
    return executor.run_all_with_marker(test_marker)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
