import pytest


# 把fixture写到xonftest.py里面，可以直接用，是共享的

class Test_Demo():
    def test_1(self):
        print('测试用例1')
        assert 11 == 11

    def test_2(self, myfixture):  # 传入了就调用fixture
        print('测试用例2')
        assert 11 == 11

    def test_3(self, myfixture):
        print('测试用例3')
        assert 11 == 11
