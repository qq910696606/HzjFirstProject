import pytest
import allure

@allure.feature('登录模块')  #功能模块
class TestLogin():
    @allure.story('登录成功') # 子功能模块
    def test_login_success(self):
        with allure.step("步骤1"):
            print("1、打开菜单")
        with allure.step("步骤2"):
            print("2、点击功能")
        print('这是登录用例，登录成功')
        assert 1==2


    @allure.story('登录失败')
    def test_login_fail(self):
        print('这是登录用例，登录失败')
        pass

    @allure.story('用户缺失')
    def test_login_none(self):
        print('这是登录用例，用户名缺失')
        pass

    @allure.testcase("https://www.baidu.com","测试失败可以开始百度了")
    def test_login_baidu(self):
        print('这是测试用例，用例可以链接到方案里面去哦')
        pass