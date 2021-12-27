import pytest


def add(a, b):
    return a + b


# 数据组合会列出所有可能的组合进行测试
@pytest.mark.parametrize(("a,b"), [(1, 2), (4, 5)], ids=["case1", "case2"])  # ids指定参数的别名
@pytest.mark.parametrize(("c"), [3, 9], ids=["case1", "case2"])  # ids指定参数的别名
def test(a, b, c):
    assert add(a, b) == c
