from Test_Framework.PlaceholderMethods import PlaceholderMethods
from Test_Framework.RestCountiresMethods import RestCountriesMethods

class Centrum(object):

    test_token = "Test Me"

    def __init__(self):
        self.placeholder = PlaceholderMethods(Centrum.test_token)
        self.countries_api = RestCountriesMethods()
