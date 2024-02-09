import unittest 
from app import add
class TestApp(unittest.TestCase):
    def test_add_two_positive_integers(self):
        res1 = add(10,20)
        self.assertEqual(res1, 30)

    def test_add_one_inte_one_str(self):
        res1 = add(10,"2")
        self.assertEqual(res1, 0)
# tc = TestApp()
# tc.test_add_two_positive_integers()
if __name__ == "__main__":
    unittest.main()
