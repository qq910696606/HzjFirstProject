import pytest
import yaml

class Testa:
    #使用list
    @pytest.mark.parametrize(['a','b'],yaml.safe_load(open("./data.yaml")))
    def test_1(self,a,b):
        print(a,type(a))
        print(a+b)

#使用list
    @pytest.mark.parametrize(('a'),[(10)])
    def test_2(self,a):
        print(a,type(a))
