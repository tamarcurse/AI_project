import unittest
import os
from File import CFile
from Data_mgr import CDataMgr
# Test for CFile class
class TestCFile(unittest.TestCase):
    def setUp(self):
        self.file = CFile()
        self.path = "any_file.txt"
        self.data = "sample text"
        with open(self.path, "w") as f:
            f.write(self.data)
    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)
    def test_set_path(self):
        self.file.set_path("../files/test.txt")
        self.assertEqual(self.file.get_path(), "../files/test.txt")
        self.assertEqual(self.file.get_name(), "test.txt")
    def test_load_data(self):
        self.file.set_path(self.path)
        self.file.load_data()
        self.assertEqual(self.file.get_data(), self.data)

class data_mgr_test(unittest.TestCase):
    def setUp(self):
        self.data_mgr = CDataMgr()
        self.file1 = CFile()
        self.file2 = CFile()
        self.file1.set_path("file1.txt")
        self.file2.set_path("file2.txt")
        with open(self.file1.get_path(), "w") as f:
            f.write("data1")
        with open(self.file2.get_path(), "w") as f:
            f.write("data2")
    def tearDown(self):
        if os.path.exists(self.file1.get_path()):
            os.remove(self.file1.get_path())
        if os.path.exists(self.file2.get_path()):
            os.remove(self.file2.get_path())
    def test_add_file(self):
        self.data_mgr.add_file(self.file1)
        self.data_mgr.add_file(self.file2)
        data = self.data_mgr.get_data()
        expected_data = "data1data2"
        self.assertEqual(data, expected_data)
    def test_remove_file(self):
        self.data_mgr.add_file(self.file1)
        self.data_mgr.add_file(self.file2)
        self.data_mgr.remove_file(self.file1)
        data = self.data_mgr.get_data()
        expected_data = "data2"
        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()
    