import unittest
import requests


class FlaskTest(unittest.TestCase):
    API = 'http://127.0.0.1:5000/'
    POINT_BODY = {
        "name": "Point 2"
    }
    POINT_BODY_UPDATE = {
        "name": "Point EDIT"
    }

    def test_1_create_point(self):
        res = requests.post(self.API + 'point', json=self.POINT_BODY)
        self.assertEqual(res.status_code, 201)

    # @unittest.expectedFailure
    def test_2_get_all_point(self):
        res = requests.get(self.API + 'point')
        self.assertEqual(res.status_code, 200)

    def test_3_update_point(self):
        id = 1
        res = requests.put(f"{self.API}point/{id}",
                           json=self.POINT_BODY_UPDATE)
        self.assertEqual(res.status_code, 200)

    def test_4_update_point(self):
        id = 1
        res = requests.delete(f"{self.API}point/{id}")
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
