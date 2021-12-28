import pytest
import yaml
# 步骤驱动
def getdata():
    with open("./data_step.yaml") as f:
        data = yaml.safe_load(f)
        select_step = data[1]
def step1():
    print("测试步骤1：登录")
def step2():
    print("测试步骤2：获取信息")
def step3():
    print("测试步骤3：进行对比")