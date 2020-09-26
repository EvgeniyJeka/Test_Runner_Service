import requests
import json
import configparser
import os


class RestCountriesMethods(object):
    # Methods of Public "Rest Countries" API on "Rapid API" portal
    # https://rapidapi.com/apilayernet/api/rest-countries-v1

    # Getting the configuration from config file
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

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

    # Returns countries data for all countries where given language is spoken
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


    # Returns countries data for all countries where given currency is used
    def get_countries_by_currency(self, currency):

        url = self.base_url + f"/currency/{currency}"

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


    # Country by capital
    def get_country_by_capital(self, capital):

        url = self.base_url + f"/capital/{capital}"

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

    # Get data on all countries
    def get_all_countries(self):

        url = self.base_url + f"/all"

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



