"""
Unit and regression test for the molssi_devops_2019 package.
"""

# Import package, test suite, and other packages as needed
import molssi_devops_2019 as md
import pytest
import sys


@pytest.mark.parametrize('string_in, string_out',[
    ('hello wOrlD', 'Hello World'),
    ('hoW Are you', 'How Are You')
])
def test_title_case(string_in, string_out):
    assert md.title_case(string_in) == string_out


def test_type_error():

    with pytest.raises(TypeError):
        md.title_case(['hello', 'world'])

def test_value_error():

    with pytest.raises(ValueError):
        md.title_case('')



