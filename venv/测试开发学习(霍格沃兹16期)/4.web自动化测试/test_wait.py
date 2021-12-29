import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://home.testing-studio.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)  # 缓冲的作用

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="所有分类"]').click()
        # time.sleep(3)
        #等待函数，可以用selenium自带的代替
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]')) >= 1
        # selenium自带的做判断
        WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable((By.XPATH,'//*[@class="table-heading"]')))
        self.driver.find_element(By.XPATH, '//*[@title="招聘内推"]').click()
        print('hello')