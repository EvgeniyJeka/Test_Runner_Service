import json

class PlaceholderRequests(object):

    @classmethod
    def create_resourse(cls, title, body, user_id):
        payload = {}
        payload['title'] = title
        payload['body'] = body
        payload['user_id'] = user_id
        return json.dumps(payload)

    @classmethod
    def update_resourse(cls, id, title, body, user_id):
        payload = {}
        payload['id'] = id
        payload['title'] = title
        payload['body'] = body
        payload['user_id'] = user_id
        return json.dumps(payload)