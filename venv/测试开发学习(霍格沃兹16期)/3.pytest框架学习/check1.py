import pytest

class Test_Demo():
    def test_1(self):
        print('测试用例1')
        assert  11==11
    def test_2(self,myfixture1): # 传入了就调用fixture
        print('测试用例2')
        re = myfixture1
        print('fix返回的参数：',re)
        assert  11==11
    def test_3(self):
        print('测试用例3')
        assert  11==11

# ;自定义测试文件命名规则
# python_files = check*
# ;自定义测试类命名规则
# python_classes = Test*
# ;自定义测试方法的规则
# python_functions = test_* check_*