import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тест фильтра по валюте
def test_filter_by_currency(transaction):
    transaction_filter = filter_by_currency(transaction, "USD")
    assert next(transaction_filter)["id"] == 939719570
    assert next(transaction_filter)["id"] == 142264268
    assert next(transaction_filter)["id"] == 895315941


# Тест фильтра по валюте (пустой список)
def test_filter_by_currency_empty(transaction_empty):
    with pytest.raises(StopIteration) as e:
        transaction_filter = filter_by_currency(transaction_empty, "USD")
        next(transaction_filter)
    assert str(e.typename) == "StopIteration"


# Тест генератора описаний
def test_transaction_descriptions(transaction):
    description = transaction_descriptions(transaction)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"


# Тест генератора описаний (пустой список)
def test_transaction_descriptions_empty(transaction_empty):
    with pytest.raises(StopIteration) as e:
        description = transaction_descriptions(transaction_empty)
        next(description)
    assert str(e.typename) == "StopIteration"


# Тест генератора номеров карт
def test_card_number_generator():
    card_number = card_number_generator(8888, 8900)
    assert next(card_number) == "0000 0000 0000 8888"


# Тест генератора номеров карт (неверный диапазон)
def test_card_number_generator_raises():
    with pytest.raises(StopIteration) as e:
        card_number = card_number_generator(5, 0)
        next(card_number)
    assert str(e.typename) == "StopIteration"
