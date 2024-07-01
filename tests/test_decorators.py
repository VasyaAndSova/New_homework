import os

import pytest

from src.decorators import log


def test_log_file():
    @log(filename="mylog.txt")
    def example_function(x, y):
        return x + y

    result = example_function(8, 10)
    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function ok. Result: 18\n"
    assert result == 18


def test_log_console(capsys):
    @log(filename=0)
    def example_function(x, y):
        return x + y

    result = example_function(1, 2)
    captured = capsys.readouterr()

    assert captured.out == "example_function ok. Result: 3\n"
    assert result == 3


def test_log_file_raise():
    @log(filename="mylog.txt")
    def example_function(x, y):
        raise TypeError("Что-то пошло не так")

    with pytest.raises(TypeError, match="Что-то пошло не так"):
        example_function("a", 6)

    with open(os.path.join(r"logs", "mylog.txt"), "rt") as file:
        for line in file:
            log_string = line

    assert log_string == "example_function TypeError: Что-то пошло не так. Inputs: ('a', 6), {}\n"
