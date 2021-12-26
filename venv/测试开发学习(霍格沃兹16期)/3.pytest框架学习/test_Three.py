import pytest
import yaml
import json

class TestDemo:
    #使用string
    @pytest.mark.parametrize("env",yaml.safe_load(open("./data2.yaml")))
    def test_1(self,env):
        if "test" in env:
            print("这是测试环境",env,type(env))
            # print('测试环境的ip为：',ret_dict["test"])
        elif "dev" in env:
            print("这是开发环境",env)
    def test_2(self):
        print(type(yaml.safe_load(open("./data2.yaml"))))