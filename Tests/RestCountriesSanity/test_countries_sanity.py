import pytest
from Test_Framework.Center import Centrum

class TestCountriesSanity(object):

    postman = Centrum()

    @pytest.mark.countries
    def test_all_countries_response_structure(self):

        response = self.postman.countries_api.get_all_countries()

        assert (type(response['content']) == list)
        assert ((type(response['content'][0])) == dict)
        assert (type(response['content'][0]['borders'] == list))



    @pytest.mark.countries
    def test_all_countries_response_contains(self):

        response = self.postman.countries_api.get_all_countries()

        for country in response['content']:
            print(country)
            assert 'name' in country.keys()
            assert 'topLevelDomain' in country.keys()
            assert 'capital' in country.keys()
            assert 'altSpellings' in country.keys()

