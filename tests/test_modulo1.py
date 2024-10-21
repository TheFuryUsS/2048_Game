import pytest
from package.modulo1 import suma

def test_suma():
    assert suma(2, 3) == 5