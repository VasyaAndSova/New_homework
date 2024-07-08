import os

from src.setup_logger import setup_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = setup_logger("masks", file_path_1)


def get_mask_card(numbers: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info(f"Задаем формат маски для номера банковской карты {numbers}")
    mask_card = f"{numbers[0:4]} {numbers[4:6]}** **** {numbers[12:]}"
    return mask_card


def get_mask_account(numbers: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info(f"Проверяем правильность написания {numbers}")
    mask_account = f"**{numbers[-4:]}"
    return mask_account
