import pytest
#autouse=True m每一个用例都会用了，不传都可以执行
# @pytest.fixture(autouse=True)
# def myfixture():
#     print('这是我的fixture')

# 设置作用域function/class/module/session,默认是function
# class 类中只运行一次
# @pytest.fixture(scope='class')
# def myfixture():
#     print('这是我的fixture2')

# 一个py文件就是一个module， 一个py文件执行一次
# @pytest.fixture(scope='module')
# def myfixture():
#     print('这是我的fixture：module')

# fixture带参数
@pytest.fixture(params=['canshu1','canshu2'])
def myfixture1(request):
    print("执行了一次fixture，参数是：%s"%request.params)
    yield request.params
    print('激活后面的操作')
