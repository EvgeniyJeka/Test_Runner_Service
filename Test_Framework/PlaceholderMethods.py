from Test_Framework.PlaceholderRequests import *
import requests
import configparser
import os


class PlaceholderMethods(object):
    # Go to https://jsonplaceholder.typicode.com/guide.html

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

    base_url = config['PLACE_HOLDER']['base_url']

    def __init__(self, test_token):
        self.headers = {"Content-type": "application/json; charset=UTF-8"}

    def list_of_all(self):

        url = self.base_url
        headers = self.headers

        try:
            response = requests.get(url, headers=headers)
            result = {}
            result['code'] = response
            result['content'] = response.json()
            return result

        except Exception as e:
            print(f"Failed to get the required data : {e}")

    def get_resource_by_id(self, id):

        url = self.base_url + f"/{id}"
        headers = self.headers
        print(f"Log: url used {url}")

        try:
            response = requests.get(url, headers=headers)
            result = {}
            result['code'] = response
            result['content'] = response.json()
            return result

        except Exception as e:
            print(f"Failed to get the required data : {e}")

    def create_resource(self, title, body, user_id):

        url = self.base_url
        headers = self.headers
        body = PlaceholderRequests.create_resourse(title, body, user_id)

        print(f"Log: url used {url}")

        try:
            response = requests.post(url, data=body, headers=headers)
            result = {}
            result['code'] = response
            result['content'] = response.json()
            return result

        except Exception as e:
            print(f"Failed to create a resource: {e}")

    def update_resource(self, id, title, body, user_id):

        url = self.base_url + f"/{id}"
        headers = self.headers
        body = PlaceholderRequests.update_resourse(id, title, body, user_id)

        print(f"Log: url used {url}")

        try:
            response = requests.put(url, data=body, headers=headers)
            result = {}
            result['code'] = response
            result['content'] = response.json()
            return result

        except Exception as e:
            print(f"Failed to update the resource: {e}")

    def delete_resource(self, id):

        url = self.base_url + f"/{id}"
        headers = self.headers
        print(f"Log: url used {url}")

        try:
            response = requests.delete(url, headers=headers)
            result = {}
            result['code'] = response
            result['content'] = response.json()
            return result

        except Exception as e:
            print(f"Failed to get the required data : {e}")

    def get_resource_by_user_id(self, id):

        url = self.base_url + f"?userId={id}"
        headers = self.headers
        print(f"Log: url used {url}")

        try:
            response = requests.get(url, headers=headers)
            result = {}
            result['code'] = response
            result['content'] = response.json()
            return result

        except Exception as e:
            print(f"Failed to get the required data : {e}")
