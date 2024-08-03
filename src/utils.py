import json
import logging
import os

import pandas as pd

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)

# Создание логера
logg = logging.getLogger(__name__)
# Создание хендлера
file_handler = logging.FileHandler(os.path.join("logs", "get_data_from_file.log"), "w")
# Создание форматера
file_formatter = logging.Formatter("%(asctime)s-%(funcName)s-%(levelname)s: %(message)s")
# Установка форматера
file_handler.setFormatter(file_formatter)
# Добавление хендлера к логеру
logg.addHandler(file_handler)
# Настройка уровня логирования
logg.setLevel(logging.DEBUG)


def get_data_financial_transactions(file_path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает данные финансовых транзакций"""
    try:
        logger.info(f"Открытие json-файла {file_path}")
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
            logger.info(f"Проверяем, что файл {file_path} не пустой")
            if isinstance(repos, list):
                return repos
            else:
                logger.info(f"Возвращаем пустой словарь, если файл {file_path} пустой")
                return []
    except Exception:
        logger.error("Ошибка")
        return []


def get_data_from_file(path: str) -> list[dict]:
    """Функция принимает путь до JSON, EXCEL или CSV файла и возвращает
    список словарей с данными о финансовых транзакциях."""
    try:
        logg.info("Определение формата файла")
        if os.path.splitext(path)[1].lower() in (".xls", ".xlsx"):
            logg.info("Excel file")
            logg.info("Попытка открытия файла")
            data_frame = pd.read_excel(path)
            logg.info("Файл открыт")
        elif os.path.splitext(path)[1].lower() == ".csv":
            logg.info("CSV file")
            logg.info("Попытка открытия файла")
            data_frame = pd.read_csv(path, sep=";")
            logg.info("Файл открыт")
        elif os.path.splitext(path)[1].lower() == ".json":
            logg.info("JSON file")
            return get_data_financial_transactions(path)
        else:
            logg.error("Ошибка формата файла")
            logg.error("Завершение программы, транзакций не найдено")
            return []
    except FileNotFoundError:
        logg.error("Ошибка открытия файла")
        logg.error("Завершение программы, транзакций не найдено")
        return []
    else:
        logg.info("Начало обработки файла")
        try:
            # Удаление пустых строк
            data_frame = data_frame[data_frame["id"].notnull()]
            logg.info("Пустые строки удалены")
            # Преобразование типа "id" в int
            data_frame["id"] = data_frame["id"].map(int)
            logg.info("id transaction -> int")
            # Преобразование типа "amount" в str
            data_frame["amount"] = data_frame["amount"].map(str)
            logg.info("amount transaction -> str")
            # Новый столбец "operationAmount"
            data_frame["operationAmount"] = data_frame.apply(
                lambda x: {"amount": x.amount, "currency": {"name": x.currency_name, "code": x.currency_code}}, axis=1
            )
            logg.info("create operationAmount")
            # Создание списка словарей
            operations = data_frame[["id", "state", "date", "operationAmount", "description", "from", "to"]].to_dict(
                "records"
            )
            logg.info("Обработка файла завершена")
        except KeyError:
            logg.error("Ошибка обработки файла")
            logg.error("Завершение программы, транзакций не найдено")
            return []

    logg.info("Успешное завершение программы")
    return operations
