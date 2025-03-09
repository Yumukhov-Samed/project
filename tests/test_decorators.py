import time
from decorators.decorators import log
from functools import wraps
import pytest

@log()
def my_function(x,y):
    return x + y

def test_my_function(capsys):
    my_function(1,2)
    captured = capsys.readouterr()
    assert 'my_function ok' in captured.out


