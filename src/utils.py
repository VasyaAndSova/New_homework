import json
import os

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "utils.log")
logger = setup_logger("utils", file_path_1)


def get_data_financial_transactions(json_file_path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает данные финансовых транзакций"""
    try:
        logger.info(f"Открытие json-файла {json_file_path}")
        with open(json_file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
            logger.info(f"Проверяем, что файл {json_file_path} не пустой")
            if isinstance(repos, list):
                return repos
            else:
                logger.info(f"Возвращаем пустой словарь, если файл {json_file_path} пустой")
                return []
    except Exception:
        logger.error("Ошибка")
        return []
