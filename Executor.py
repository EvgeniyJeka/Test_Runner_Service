import os
from os import listdir
import pytest
from pytest_jsonreport.plugin import JSONReport
import logging

repo_dir = os.path.dirname(__file__)
TESTS_DIRECTORY = os.path.join(repo_dir, "Tests")


class TestExecutor(object):
    plugin = JSONReport()



    def run_test_file(self, file_name):
        """
        This method receives a filename with py extension.
        The file is expected to contain Pytest tests.
        The file will be searched, once it is found all the tests in that file will be executed.
        Test execution report created by JSONReport plugin is created.
        :param file_name: file name, String
        """

        logging.info(f'Executor: File named {file_name} was received ')

        # List of all paths of all files and directories
        folder_list = os.walk(TESTS_DIRECTORY)

        # Looking for the path of the requested file. Running the tests once the file is found.
        for folder in folder_list:
            if file_name in folder[2]:
                to_run = os.path.join(folder[0], file_name)
                logging.info(f'Executer: Requested file location: {to_run}')

                pytest.main([to_run], plugins=[self.plugin])

                logging.info(f'Executor: Test execution report: {self.compose_testrun_report(self.plugin.report)}')
                return self.compose_testrun_report(self.plugin.report)

    def run_test_folder(self, folder_name):
        """
        The method receives a folder name. The folder is expected to contain test files with 'py' extension.
        Once the folder is found all the test files are executed
        :param folder_name: String
        :return: test execution reports, JSON dict of dicts
        """
        logging.info(f'Executor: File named {folder_name} was received ')

        # List of all paths of all files and directories
        folder_list = os.walk(TESTS_DIRECTORY)

        # Iterating over all folders in tests directory to find the requested folder
        for folder in folder_list:

            if folder_name in folder[1]:
                extracted_folder_path = os.path.join(folder[0], folder_name)
                logging.info(f'Executor: Requested folder location {extracted_folder_path}')

                # Gathering all files from the folder
                files = [f for f in listdir(extracted_folder_path)
                         if os.path.isfile(os.path.join(extracted_folder_path, f))]

                # Running all test files in the requested folder, returning a list of report
                report = self.run_several_files(files, extracted_folder_path)
                logging.info(f'Executor: Test execution report: {report}')
                return report

    def run_all_with_marker(self, marker: str):
        """
        The method receives a pytest marker and executes all tests that are marked with it
        :param marker: String
        :return : JSON report
        """

        logging.info(f'Received the following test marker: {marker}')

        curr_dir = os.getcwd()

        # !! move to config
        os.chdir(".\Tests")

        to_execute = f"-v -k {marker}"
        pytest.main(to_execute.split(" "), plugins=[self.plugin])

        logging.info(f'Executor: Test execution report: {self.compose_testrun_report(self.plugin.report)}')

        os.chdir(curr_dir)
        return self.compose_testrun_report(self.plugin.report)

    def run_several_files(self, files_list: list, base_path):
        """
        This method is used to execute several test files. Returns a JSON execution report
        :param base_path: path of all files in files_list
        :param files_list: list of test file names
        :return: dict. Keys: executed file names, Values: execution report
        """
        result = {}

        # Executing only files with '.py' extension
        python_files_list = [f for f in files_list if len(f.split(".")) > 1 and f.split(".")[1] == 'py']

        # For each file full path is built, after that the file is executed - can be done from any dir
        for file in python_files_list:
            executed_file_full_path = os.path.join(base_path, file)
            pytest.main([executed_file_full_path], plugins=[self.plugin])
            result[file] = self.compose_testrun_report(self.plugin.report)

        return result

    @staticmethod
    def compose_testrun_report(original_plugin_report):
        """
        The JSONReport plugin generates a report that is quite cumbersome.
        This method is used to extract the required data from the original JSONReport
        :param raw_data:
        """

        if not original_plugin_report['tests']:
            return {'error': f'file contains no valid pytest tests that can be executed'}

        # Adding environment data, test run summary and file name to the produced report
        result = {'environment': [original_plugin_report['environment']['Python'],
                                  original_plugin_report['environment']['Platform']],
                  'summary': original_plugin_report['summary'], 'results': {},
                  'file': original_plugin_report['tests'][0]['nodeid'].split("::")[0]}

        # Adding the result (a.k.a. "outcome") of each test to the produced report
        for item in original_plugin_report['tests']:
            result['results'][item['nodeid'].split("::")[2]] = item['outcome']

        return result


if __name__ == '__main__':

    executer = TestExecutor()

    print(TESTS_DIRECTORY)
    executer.run_all_with_marker("smoke")
