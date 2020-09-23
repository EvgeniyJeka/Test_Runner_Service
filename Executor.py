import os
from os import listdir
import pytest
from pytest_jsonreport.plugin import JSONReport
import logging


class TestExecutor(object):


    def get_list_of_files(self, dirName):

        # create a list of file and sub directories
        # names in the given directory
        list_of_file = os.listdir(dirName)
        allFiles = list()

        # Iterate over all the entries
        for entry in list_of_file:
            # Create full path
            fullPath = os.path.join(dirName, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(fullPath):
                allFiles = allFiles + self.get_list_of_files(fullPath)
            else:
                allFiles.append(fullPath)

        return allFiles

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
        files_list = self.get_list_of_files(".")
        plugin = JSONReport()


        for item in files_list:

            if file_name in item:
                # Extracting the file path once the file is found
                extract_file_path = item.split("\\")
                extract_file_path.pop(len(extract_file_path) - 1)

                # Going to the extracted paths and running the tests
                original_workdir = os.getcwd()
                os.chdir("/".join(extract_file_path))
                pytest.main([file_name], plugins=[plugin])

                os.chdir(original_workdir)
                return self.compose_testrun_report(plugin.report)

    def run_test_folder(self, folder_name):

        # List of all paths of all files and directories
        files_list = executor.get_list_of_files(".")



        for item in files_list:

            if folder_name in item:
                # Extracting the file path once the file is found
                extract_folder_path = item.split("\\")
                extract_folder_path.pop(len(extract_folder_path) - 1)
                print("/".join(extract_folder_path))

                # Going to the extracted paths and running the tests
                os.chdir("/".join(extract_folder_path))
                files = [f for f in listdir(".") if os.path.isfile(f)]

                # Running all test files in the requested folder, returning a list of report
                report = self.run_several_files(files)
                return report

    def run_several_files(self, files_list: list):
        """
        This method is used to execute several test files. Returns a JSON execution report
        :param files_list: list of test file names
        :return:
        """
        result = []
        plugin = JSONReport()

        for file in files_list:
            pytest.main([file], plugins=[plugin])
            result.append(self.compose_testrun_report(plugin.report))

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

    executor = TestExecutor()

    raw = executor.run_test_file('test_countries_sanity.py')

    print(raw)

    raw = executor.run_test_file('test_placeholder_sanity.py')

    print(raw)
