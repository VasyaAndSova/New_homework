from src.processing import (count_transactions_by_category, filter_by_line_in_description, get_dict_by_key_state,
                            get_dict_date_dicrease)


#  Тест функции фильтра, случай пустого списка
def test_filter_state_operations_empty(transaction_empty):
    assert get_dict_by_key_state(transaction_empty) == []


#  Тест функции фильтра по статусу исполнено
def test_filter_state_operations_executed(transaction_total, transaction_executed):
    assert get_dict_by_key_state(transaction_total) == transaction_executed


# Тест функции фильтра по статусу отменено
def test_filter_state_operations_cancaled(transaction_total, transaction_canceled):
    assert get_dict_by_key_state(transaction_total, "CANCELED") == transaction_canceled


# Тест функции сортировки даты по убыванию
def test_sorted_date_operations_decreasing(transaction_total):
    sequence = get_dict_date_dicrease(transaction_total)
    assert sequence[0]["date"] > sequence[-1]["date"]


# Тест функции сортировки даты по возрастанию
def test_sorted_date_operations(transaction_total):
    sequence = get_dict_date_dicrease(transaction_total, False)
    assert sequence[0]["date"] < sequence[-1]["date"]


# Тест функции поиска по фразе
def test_filter_by_line_in_description(transaction):
    result = filter_by_line_in_description(transaction, "организации")
    assert "организации" in result[0]["description"]
    assert len(result) == 2
    assert result[1]["id"] == 594226727


# Тест функции поиска по фразе пустой список
def test_filter_by_line_in_description_empty(transaction):
    result = filter_by_line_in_description(transaction, "не найдено")
    assert result == []


# Тест функции подсчета транзакций по категориям
def test_count_transactions_by_category(transaction):
    result = count_transactions_by_category(
        transaction, ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    )
    assert result == {"Перевод организации": 2, "Перевод со счета на счет": 2, "Перевод с карты на карту": 1}
