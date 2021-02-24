import pytest
from functions import my_function

def test1():
    result_code, result_value = my_function(10,10,10)
    assert result_code == 1 and result_value == 90

def test2():
    result_code, result_value = my_function(100,10,10)
    assert result_code == 1 and result_value == 990

def test3():
    result_code, result_value = my_function("aa",10,10)
    assert result_code == 0

def test4():
    result_code, result_value = my_function(100,10,"10")
    assert result_code == 0
