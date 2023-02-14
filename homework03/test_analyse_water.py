from analyze_water import  turbidity, threshold
import pytest

def test_func1():
    assert turbidity( info_to_pass_to_func1 ) == expected_value

def test_func2():
    assert threshold( info_to_pass_to_func2 ) == expected_value
