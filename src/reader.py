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
    dict_xlsx = []
    for column_name, column_data in df.iterrows():
        m = {
            "id": column_data["id"],
            "state": column_data["state"],
            "date": column_data["date"],
            "amount": column_data["amount"],
            "currency_name": column_data["currency_name"],
            "currency_code": column_data["currency_code"],
            "from": column_data["from"],
            "to": column_data["to"],
            "description": column_data["description"],
        }
        dict_xlsx.append(m)

    return dict_xlsx
