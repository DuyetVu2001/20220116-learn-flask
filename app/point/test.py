import unittest
import requests


class PointTest(unittest.TestCase):
    '''
    create (201) => create duplicate (409) => create missing filed(400) => create empty value (409) => get => update => delete 
    '''
    point_id = 1
    API = 'http://127.0.0.1:5000/'
    BODY_CREATE = {"name": "Point 2"}
    BODY_UPDATE = {"name": "Point EDIT"}
    BODY_EMPTY_VALUE = {"name": ""}

    def test_create(self):
        res = requests.post(self.API + 'point', json=self.BODY_CREATE)
        self.assertEqual(res.status_code, 201)

    def test_create_duplicate(self):
        res = requests.post(self.API + 'point', json=self.BODY_CREATE)
        self.assertEqual(res.status_code, 409)

    def test_create_empty(self):
        res = requests.post(self.API + 'point', json=self.BODY_EMPTY_VALUE)
        self.assertEqual(res.status_code, 400)

    # @unittest.expectedFailure
    def test_get_all(self):
        res = requests.get(self.API + 'point')
        self.point_id = res.json()[0]['id']
        self.assertEqual(res.status_code, 200)

    def test_update(self):
        res = requests.put(
            f"{self.API}point/{self.point_id}", json=self.BODY_UPDATE)
        self.assertEqual(res.status_code, 200)

    def test_delete(self):
        res = requests.delete(f"{self.API}point/{self.point_id}")
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()


# # check if response is 200
# def test_index(self):
#     tester = app.test_client(self)
#     response = tester.get('/hello')
#     status_code = response.status_code
#     self.assertEqual(status_code, 200)

# # check if content return is application/json
# def test_index_content(self):
#     tester = app.test_client(self)
#     response = tester.get('/hello')
#     self.assertEqual(response.content_type, 'application/json')

# # check for data return
# def test_index_data(self):
#     tester = app.test_client(self)
#     response = tester.get('/hello')
#     self.assertTrue(b"data" in response.data)
