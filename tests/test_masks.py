
import pytest

from src.masks import mask_account_number, mask_card_number
from tests.mask_test_data import account_test_data, card_test_data


# Тест функции маскировки счетов
@pytest.mark.parametrize("number, result", account_test_data)
def test_mask_account_number(number, result):
    # Если ожидается неверный тип входных данных
    if result == "TypeError":
        with pytest.raises(TypeError) as e:
            mask_account_number(number)
        assert str(e.typename) == result
    # Если ожидается неверный формат входых данных
    elif result == "ValueError":
        with pytest.raises(ValueError) as e:
            mask_account_number(number)
        assert str(e.typename) == result
    # Если ожидаются корректные входные данные
    else:
        assert mask_account_number(number) == result


# Тест функции маскировки карт
@pytest.mark.parametrize("number, result", card_test_data)
def test_mask_card_number(number, result):
    # Если ожидается неверный тип входных данных
    if result == "TypeError":
        with pytest.raises(TypeError) as e:
            mask_card_number(number)
        assert str(e.typename) == result
    # Если ожидается неверный формат входых данных
    elif result == "ValueError":
        with pytest.raises(ValueError) as e:
            mask_card_number(number)
        assert str(e.typename) == result
    # Если ожидаются корректные входные данные
    else:
        assert mask_card_number(number) == result
