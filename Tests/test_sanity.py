import pytest
from Test_Framework.Center import Centrum


class TestSanity(object):

    postman = Centrum()

    @pytest.mark.smoke
    def test_response_code(self):

        response = self.postman.placeholder.list_of_all()

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


    @pytest.mark.content
    def test_ids_consistent(self):

        response = self.postman.placeholder.list_of_all()

        assert len(response['content']) == 100

        cnt = 1

        for item in response['content']:
            assert item['id'] == cnt
            cnt += 1







