import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(20)

    def teardown(self):
        time.sleep(2)
        self.driver.close()

    def test_css(self):
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('胡智杰')
        self.driver.find_element(By.CSS_SELECTOR,'#su').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,'#kw').send_keys('胡智杰')
        self.driver.find_element(By.CSS_SELECTOR,'#kw').screenshot('hzj.png')
