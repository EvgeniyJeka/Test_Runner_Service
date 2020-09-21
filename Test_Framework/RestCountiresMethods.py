import requests
import json
import configparser


class RestCountriesMethods(object):
    # Methods of Public "Rest Countries" API on "Rapid API" portal

    # Getting the configuration from config file
    config = configparser.ConfigParser()
    config.read("../Test_Framework/config.ini")

    base_url = (config['REST_COUNTRIES']["base_url"])
    host = (config['REST_COUNTRIES']["host"])
    key = (config['REST_COUNTRIES']["api_key"])

    # Returns country data by country name
    def get_country_by_name(self, name):

        url = self.base_url + f"/name/{name}"

        headers = {}
        headers['X-RapidAPI-Host'] = self.host
        headers['X-RapidAPI-Key'] = self.key

        try:
            response = requests.get(url, headers=headers)
            result = {}
            result['code'] = response
            result['content'] = response.json()
            return result

        except Exception as e:
            print(f"Failed to get the required data : {e}")

    def get_countries_by_language(self, language):

        url = self.base_url + f"/lang/{language}"

        headers = {}
        headers['X-RapidAPI-Host'] = self.host
        headers['X-RapidAPI-Key'] = self.key

        try:
            response = requests.get(url, headers=headers)
            result = {}
            result['code'] = response
            result['content'] = response.json()
            return result

        except Exception as e:
            print(f"Failed to get the required data : {e}")
