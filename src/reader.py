import csv
from typing import Any

import openpyxl


def read_csv_file(tr_reader: Any) -> Any:
    """Функция реализовывает считывание финансовых операций из CSV-файла"""
    with open("data/transactions.csv") as file:
        reader = csv.DictReader(file, delimiter=";")
        dict_csv = []
        for row in reader:
            dict_csv.append(row)
    return dict_csv


def read_xlsx_file(df: Any) -> Any:
    """Функция реализовывает считывание финансовых операций из XLSX-файла"""
    workbook = openpyxl.load_workbook("data/transactions_excel.xlsx")
    sheet = workbook.active
    dict_xlsx = []
    for row in sheet.iter_rows(values_only=True):
        dict_xlsx.append(row)
    return dict_xlsx
