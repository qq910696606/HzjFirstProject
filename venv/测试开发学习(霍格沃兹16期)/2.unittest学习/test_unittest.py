import unittest

class Demo(unittest.TestCase):

    def setUp(self) -> None:
        print('set up')

    def tearDown(self) -> None:
        print('teardown')

    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDown class')

    def test_aaa(self):
        print('测试用例1')

    def test_vvv(self):
        print('测试用例2')

    def test_bbb(self):
        print('测试用例3')

if __name__ == '__main__':
    unittest.main()