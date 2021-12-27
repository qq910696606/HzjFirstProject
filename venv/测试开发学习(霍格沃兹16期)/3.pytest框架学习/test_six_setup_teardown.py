import pytest
# module级别，文件执行的开头一次，结束一次
def setup_module():
    print('整个test*.py开始的时候只执行一次')

def teardown_module():
    print('整个test*.py结束的时候只执行一次')

#类外面的测试用例
def setup_function():
    print('不在类里面的测试用例开始就执行这个')
def teardown_function():
    print('不在类里面的测试用例结束就执行这个')

def test_3():
    print('测试用例3')
def test_4():
    print('测试用例4')

class TestHzj():
    #类级别
    def setup_class(self):
        print('类里面的所有用例开始都要一次')
    def teardown_class(self):
        print('类里面的所有用例结束都要一次')


    # 方法级别
    def setup_method(self):
        print('每一个用例开始都要呢')
    def teardown_method(self):
        print('每一个用例结束都要呢')


    def test_1(self):
        print("这是第一个测试用例")
    def test_2(self):
        print("这是第二个测试用例")