import os

from src.generators import filter_by_currency
from src.processing import filter_by_line_in_description, get_dict_by_key_state, get_dict_date_dicrease
from src.utils import get_data_from_file
from src.widget import format_date, format_requesite


def file_selection() -> list[dict]:
    """Функция запрашивает у пользователя файл для получения информации
    и возвращает данные о транзакциях из соответствующего файла"""
    while True:
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")
        answer = input(">>").upper()
        answer_options = {"1": "operations.json", "2": "transactions.csv", "3": "transactions_excel.xlsx"}
        if answer in answer_options:
            print(f"Для обработки выбран файл «{answer_options[answer]}».\n")
            return get_data_from_file(os.path.join("data", answer_options[answer]))
        else:
            print(f"Пункт меню «{answer}» не доступен.\n")


def state_selection(transactions: list[dict]) -> list[dict]:
    """Функция принимает данные о транзакциях,  запрашивает у пользователя
    статус для фильтрации и возвращает данные отфильтрованные по
    соответствующему статусу"""
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        answer = input(">>").upper()
        if answer in ("EXECUTED", "CANCELED", "PENDING"):
            print(f"Операции отфильтрованы по статусу «{answer}».\n")
            return get_dict_by_key_state(transactions, answer)
        else:
            print(f"Статус операции «{answer}» не доступен.\n")


def sorted_selection(transactions: list[dict]) -> list[dict]:
    """Функция принимает данные о транзакциях,  запрашивает у пользователя
    необходимость и направление сортировки по дате и возвращает данные,
    соответсвенно отсортированные"""
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        answer = input(">>").upper()
        if answer in ("ДА", "Д", "YES", "Y"):
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                answer = input(">>").upper()
                if answer in ("ПО ВОЗРАСТАНИЮ", "ВОЗРАСТАНИЮ", "ВОЗРАСТАНИЕ"):
                    print("Выбрана сортировка по возрастанию.\n")
                    return get_dict_date_dicrease(transactions, False)
                elif answer in ("ПО УБЫВАНИЮ", "УБЫВАНИЮ", "УБЫВАНИЕ"):
                    print("Выбрана сортировка по убыванию.\n")
                    return get_dict_date_dicrease(transactions, True)
                else:
                    print("Некорректный ввод.\n")
        elif answer in ("НЕТ", "Н", "NO", "N"):
            print("Выбрано: без сортировки.\n")
            return transactions
        else:
            print("Некорректный ввод.\n")


def currency_selection(transactions: list[dict]) -> list[dict]:
    """Функция принимает данные о транзакциях,  запрашивает у пользователя
    необходимость вывода только рублевых операций и возвращает данные с,
    соответствено исключенными (или нет), транзакциям"""
    while True:
        print("Выводить только рублевые тразакции? Да/Нет")
        answer = input(">>").upper()
        if answer in ("ДА", "Д", "YES", "Y"):
            print("Выбраны только рублевые транзакции.\n")
            return list(filter_by_currency(transactions, "RUB"))
        elif answer in ("НЕТ", "Н", "NO", "N"):
            print("Выбраны все транзакции.\n")
            return transactions
        else:
            print("Некорректный ввод.\n")


def descrintion_selection(transactions: list[dict]) -> list[dict]:
    """Функция принимает данные о транзакциях,  запрашивает у пользователя
    ключевое слово(а) из описания для фильтрации и возвращает данные, содержащие
    данную строку"""
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        answer = input(">>").upper()
        if answer in ("ДА", "Д", "YES", "Y"):
            answer = input("Введите слово для фильтрации: ")
            print(f"Фильтрация по слову «{answer}».\n")
            return filter_by_line_in_description(transactions, answer)
        elif answer in ("НЕТ", "Н", "NO", "N"):
            print("Без фильтрации.\n")
            return transactions
        else:
            print("Некорректный ввод.\n")


def show_transaction(transaction: dict) -> None:
    """Функция принимает транзакцияю, форматирует и выводит ее в консоль"""
    # Вывод даты и описания
    print(format_date(transaction["date"]), transaction["description"])
    # Вывод источника (если есть) и назначения
    source = str(transaction.get("from"))
    target = transaction["to"]
    if source != "nan" and source != "None":
        print(format_requesite(source), end=" -> ")
    print(format_requesite(target))
    # Вывод суммы
    print(transaction["operationAmount"]["amount"], end=" ")
    print(transaction["operationAmount"]["currency"]["name"] + "\n")


def main() -> None:
    """Главная функция"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n")
    transactions = file_selection()  # Выбор и чтение файла
    transactions = state_selection(transactions)  # Выбор и фильтрация по статусу
    transactions = sorted_selection(transactions)  # Выбор и сортировка по дате
    transactions = currency_selection(transactions)  # Выбор и фильтрация по валюте
    transactions = descrintion_selection(transactions)  # Фильтрация по фразе в описании

    print("Распечатываю итоговый список транзакций...\n")
    if transactions:
        print(f"Всего банковских операций в выборке: {len(transactions)}.\n")
        for transaction in transactions:
            show_transaction(transaction)
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()
