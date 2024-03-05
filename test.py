import unittest

class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('This is a setupclass teardown ')

    def setUp(self):
        print('This a setup ')
    def testA(self):
        print('This is a test A')
    def testB(self):
        print('This is a test B')
    def testC(self):
        print('This is a test C')
    def tearDown(self):
        print('This is teardown')
    @classmethod
    def tearDownClass(cls):
        print('This is a Teardown class')

if __name__ == '__main__':
    unittest.main()