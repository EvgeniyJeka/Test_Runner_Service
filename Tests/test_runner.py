import pytest
from Test_Framework.Center import Centrum


class TestRunner(object):

    report = {}

    postman = Centrum()


    # def run_all_tests(self):
    #     pytest.main("-v test_sanity.py".split(" "))
    #     time.sleep(3)
    #     print(self.report)


    @pytest.mark.smoke
    def test_response_code(self):

        response = self.postman.placeholder.list_of_all()

        print("Updating report")

        self.report['Response_code'] = "XXX"

        assert response['code'].status_code == 200

    @pytest.mark.smoke
    def test_resposne_type(self):

        response = self.postman.placeholder.list_of_all()

        assert type(response['content']) == list

        for item in response['content']:
            assert type(item) == dict


    @pytest.mark.smoke
    def test_response_structure(self):

        response = self.postman.placeholder.list_of_all()

        for item in response['content']:
            assert 'userId' in item.keys()
            assert 'id' in item.keys()
            assert 'title' in item.keys()
            assert 'body' in item.keys()

        print(self.report)



    @pytest.mark.content
    def test_ids_consistent(self):

        response = self.postman.placeholder.list_of_all()

        assert len(response['content']) == 100

        cnt = 1

        for item in response['content']:
            assert item['id'] == cnt
            cnt += 1







