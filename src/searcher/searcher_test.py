import unittest
from model import CModel
class TestModel(unittest.TestCase):
    def setUp(self):
        self.model = CModel()
    def test_get_response(self):
        input_text = "Hello, how are you?"
        response = self.model.get_response(input_text)
        self.assertIsInstance(response, str)
        self.assertNotEqual(response, "")
        print("Response from model:", response)
if __name__ == '__main__':
    unittest.main()