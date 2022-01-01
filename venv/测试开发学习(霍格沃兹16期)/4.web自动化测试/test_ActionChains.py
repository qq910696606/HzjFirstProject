from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from time import sleep

from selenium.webdriver.common.by import By


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        # 获取到3个元素
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_right_click = self.driver.find_element_by_xpath('//input[@value="right click me"]')
        # 定义ActionChains方法
        action = ActionChains(self.driver)
        action.click(element_click)
        action.context_click(element_right_click)
        action.double_click(element_doubleclick)
        action.perform()
        sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com')
        ele = self.driver.find_element(By.ID,"s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        # self.driver.get('https://www.baidu.com')
        # drag_element = self.driver.find_element(By.CSS_SELECTOR,'#hotsearch-content-wrapper li:nth-child(1)>a')
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element(By.ID,'dragger')
        drop_element = self.driver.find_element(By.XPATH,'/html/body/div[3]')

        action = ActionChains(self.driver)
        # action.drag_and_drop(drag_element,drop_element).perform()
        # action.click_and_hold(drag_element).release(drop_element).perform()
        action.click_and_hold(drag_element).move_to_element(drop_element).release().perform()
        sleep(3)
if __name__ == '__main__':
    pytest.main(['-sv','test_ActionChains.py'])