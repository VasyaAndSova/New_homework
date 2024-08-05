import pytest

from src.widget import format_date, format_requesite
from tests.mask_test_data import format_requesite_test_data


# Тест функции форматирования реквезитов
@pytest.mark.parametrize("id_number, result", format_requesite_test_data)
def test_format_requesite(id_number, result):
    # Если ожидается неверный тип входных данных
    if result == "TypeError":
        with pytest.raises(TypeError) as e:
            format_requesite(id_number)
        assert str(e.typename) == result
    # Если нет номера (неверный формат стоки)
    elif result == "IndexError":
        with pytest.raises(IndexError) as e:
            format_requesite(id_number)
        assert str(e.typename) == result
    # Если ожидается неверный формат входых данных
    elif result == "ValueError":
        with pytest.raises(ValueError) as e:
            format_requesite(id_number)
        assert str(e.typename) == result
    # Если ожидаются корректные входные данные
    else:
        assert format_requesite(id_number) == result


# Тест функции форматирования даты (неверный формат)
def test_format_gate_raise_value():
    with pytest.raises(ValueError) as e:
        format_date("неверны формат")
    assert str(e.typename) == "ValueError"


# Тест функции форматирования даты (неверный тип)
def test_format_gate_raise_type():
    with pytest.raises(TypeError) as e:
        format_date(12345)
    assert str(e.typename) == "TypeError"


# Тест функции форматирования даты (ожидаемый реззультат)
def test_format_gate():
    assert format_date("2018-07-11T02:26:18.671407") == "11.07.2018"
