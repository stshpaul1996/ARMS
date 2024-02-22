import unittest

class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("this is setUpClass")

    def setUp(self):
        print("this is setUp")

    def test1(self):   #Name starts with test for all test cases
        print("this is test1")

    def test2(self):
        print("this is test2")

    def test3(self):
        print("this is test3")

    def tearDown(self):
        print("this is tearDown")

    @classmethod
    def tearDownClass(cls):
        print("this is tearDownClass")


unittest.main()