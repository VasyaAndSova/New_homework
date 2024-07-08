import json


def get_data_financial_transactions(file_path: str) -> list[dict]:
    """Функция, которая возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
            if isinstance(repos, list):
                return repos
            else:
                return []
    except Exception as e:
        print(f"Ошибка {e}")
        return []
