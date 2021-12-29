import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo():
    def setup(self):
        self.dirver = webdriver.Chrome()
        self.dirver.get('https://www.baidu.com')
        self.dirver.implicitly_wait(5)
    def teardown(self):
        self.dirver.quit()

    def test_1(self):
        self.dirver.find_element(By.ID,"kw").send_keys('github')
        self.dirver.find_element(By.ID,"su").click()
        self.dirver.find_element(By.ID,"1")

