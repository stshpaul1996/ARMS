import unittest

class SampleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #write login code
        print('hello')
        # r=self.client.post('/role/',data={"name":"user5"})
        # cls.role_id=r.json().get('id')

    def setUp(self):
        print("setup")

    def test_1(self):
        print('this is test1')
    
    def test_2(self):
        print('this is test2')

    def test_3(self):
        print('this is test3')

    def tearDown(self):
        print('this is teardown')

    @classmethod
    def tearDownClass(cls):
        print('this is teardown class')

if __name__=='__main__':
    unittest.main()