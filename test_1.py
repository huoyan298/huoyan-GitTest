# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import pytest

class Test1():
    @pytest.mark.dependency(name="a")
    def test_1(self):
        assert  True

    @pytest.mark.dependency(depends=["a"])
    def test_2(self):
        assert True


# class Test2():
#  @pytest.mark.dependency(depends=['m'])
#  def test_1(self):
#         assert True
#
#  @pytest.mark.dependency(name="m")
#  def test_2(self):
#         assert True

class Test3():
    @pytest.mark.dependency(depends=['b'])
    def test_1(self):
        assert  True

    @pytest.mark.run(order=0)
    @pytest.mark.dependency(name="b")
    def test_2(self):
        assert  True





if __name__ =="__main__":
    pytest.main(["-v","-s","test_1.py"])