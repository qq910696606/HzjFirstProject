import pytest


def func(x):
    return x + 1

#使用string参数
@pytest.mark.parametrize('a,b', [
    (1, 2),
    (2, 3),
    (34, 35),
    (4, 5)
])
def test_3(a, b):
    print(a,type(a))
    assert func(a) == b


# pytest解释器运行
def test_answer():
    assert func(3) == 4

# pytest的装饰器
@pytest.fixture()
def login():
    username='胡智杰'
    print('方法里面的输出',username)
    return username

class Test_demo:
    # 测试用例1先去执行login函数再进行测试
    def test_1(self,login):
        print(f'测试用例1,username={login}')

    def test_2(self):
        print('测试用例2')

    def c(self):
        print('不符合规则，无效的测试用例')


# python解释器运行
if __name__ == "__main__":
    pytest.main(['test_One.py', "-v"])  # 使用python解释器指定测试类
