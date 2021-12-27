#测试代码
from python_code.calculator import Calculator
import pytest

class TestClass():
    def setup_class(self):
        print('开始计算')
        self.cal = Calculator()

    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize("a,b,nums",[
        (3,5,8),(2,3,5),(300,400,700)
    ])
    def test_add(self,a,b,nums):
        print('开始计算加法')
        assert nums == self.cal.add(a,b)


    @pytest.mark.parametrize("a,b,nums",[
        (8,5,3),(5,3,2),(700,400,300)
    ])
    def test_sub(self,a,b,nums):
        assert nums == self.cal.sub(a,b)