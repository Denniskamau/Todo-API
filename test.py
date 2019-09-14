import unittest
import json
import os
import api


BASE_URL = 'http://127.0.0.1:5000/api/'
GET_URL ='http://127.0.0.1:5000/api/1'
UPDATE_URL ='http://127.0.0.1:5000/api/1'
DELETE_URL ='http://127.0.0.1:5000/api/1'
class MyApiTestCase(unittest.TestCase):

    def setup(self):
        self.api = api.app.test_client()
        self.api.testing = True
        todo =        {
        'title': u'Finish Api',
        'description': u'Finish this api and submit',
        'done': False
        }

    def test_todo_creation(self):
        todo = {
        'title': u'Finish Api',
        'description': u'Finish this api and submit',
        'done': False
        }
        response = self.api.post(BASE_URL,
                                 data=json.dumps(todo),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_todo_get_all(self):
        response = self.api.get(BASE_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['todos']), 2)

    def test_todo_get_one(self):
        response = self.api.get(GET_URL)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['todos'][0]['title'], 'Finish Api')

    def test_todo_update(self):
        todo = {
        'title': u'Finish Learning',
        'description': u'Finish this api and submit',
        'done': False
        }
        response = self.api.put(UPDATE_URL,
                                data=json.dumps(todo),
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['todo']['title'],'Finish Learning')

    def test_todo_delete(self):
        response = self.api.delete(DELETE_URL)
        self.assertEqual(response.status_code, 204)

if __name__ == "__main__":
    unittest.main()