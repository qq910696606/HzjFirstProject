#测试代码
from python_code.calculator import Calculator
import pytest
import yaml
#定义函数封装获取的数据
def get_datas():
    with open("./data3.yaml") as f:
        datas = yaml.safe_load(f)
        addatas = datas["dates"]
        addid = datas["myid"]
        print(datas)
        return [addatas,addid]

class TestClass():

    def setup_class(self):
        print('开始计算')
        self.cal = Calculator()

    def teardown_class(self):
        print('结束计算')

    @pytest.mark.parametrize("a,b,nums",[
        (2,3,5),(300,400,700)
    ])
    def test_add(self,a,b,nums):
        print('开始计算加法')
        assert nums == self.cal.add(a,b)
    # pytest.ini 可以配置消除warnning
    @pytest.mark.kkk # pytest -vs -m "kkk" test_seven_calculator.py 运行指定标记的测试用例
    @pytest.mark.demo # pytest -vs -m "demo" test_seven_calculator.py 运行指定标记的测试用例，可以打多个标签
    # 数据驱动 ，下面比较麻烦且易错
    # @pytest.mark.parametrize("a,b,nums",yaml.safe_load(open('./data3.yaml'))["dates"],ids=yaml.safe_load(open('./data3.yaml'))["myid"])
    # 可以封装读文件的方法
    @pytest.mark.parametrize("a,b,nums", get_datas()[0],
                             ids=get_datas()[1])
    def test_sub(self,a,b,nums):
        assert nums == self.cal.add(a,b)

    # pytest -vs -k "add" test_seven_calculator.py 根据用例名字筛选
    # pytest --collect-only test_seven_calculator.py 查看编写的用例