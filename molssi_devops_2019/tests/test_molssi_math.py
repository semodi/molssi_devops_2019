"""
Unit and regression test for the molssi_devops_2019 package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys

@pytest.fixture
def num_list_3():
    return [1,2,3,4,5]

@pytest.mark.parametrize('num_list, expected_mean',[
    ([1,2,3,4,5],3),
    ([0,2,4,6],3),
    ([1,2,3,4], 2.5)
])

def test_many(num_list, expected_mean):
    assert md.mean(num_list) == expected_mean

def test_mean(num_list_3):
    
    observed = md.mean(num_list_3)
    expected = 3

    assert observed == expected

def test_mean_type_error():

    test_variable = 'this is a string'

    with pytest.raises(TypeError):
        md.mean(test_variable)
