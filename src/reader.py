from typing import Any

import pandas as pd


def read_csv_file(file_path: Any) -> Any:
    """Функция реализовывает считывание финансовых операций из CSV-файла"""
    tr_reader = pd.read_csv("data/transactions.csv", delimiter=";")
    return tr_reader


def read_xlsx_file(file_path: Any) -> Any:
    """Функция реализовывает считывание финансовых операций из XLSX-файла"""
    df = pd.read_excel("data/transactions_excel.xlsx")
    return df
