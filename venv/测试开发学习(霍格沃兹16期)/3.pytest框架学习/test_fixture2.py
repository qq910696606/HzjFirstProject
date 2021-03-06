import pytest
import time
class Test_Demo():
    def test_1(self):
        print('测试用例1')
        assert  11==11
    def test_2(self,myfixture1): # 传入了就调用fixture
        print('测试用例2')
        re = myfixture1
        print('fix返回的参数：',re)
        assert  11==11

    @ pytest.mark.flaky(reruns=5,reruns_delay=0)
    def test_3(self):
        print('测试用例3')
        pytest.assume(11==11)
        time.sleep(2)
        print('11=11')
        pytest.assume(1 == 1)
        print('1=1')
        # pytest --reruns 5 --reruns-delay 1 test_fixture2.py 失败重试5次

    # 多重校验
