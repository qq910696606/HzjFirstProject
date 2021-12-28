import pytest

class Test_Demo():
    def test_1(self):
        print('测试用例1')
        assert  11==11
    def test_2(self,myfixture1): # 传入了就调用fixture
        print('测试用例2')
        assert  11==11
    def test_3(self,myfixture1):
        print('测试用例3')
        assert  11==11