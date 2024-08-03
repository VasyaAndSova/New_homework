import re
from datetime import datetime

from src.masks import mask_account_number, mask_card_number


def format_requesite(id_number: str) -> str:
    """Функция принимает строку с типом и номером карты или счета и возвращает ее,
    отформатированную и замаскированную, соответствено типу карты или счета"""
    id = re.split(r"(?=\d)", id_number, 1)[0]
    number = re.split(r"(?=\d)", id_number, 1)[1].replace(" ", "")

    if id == "Счет ":
        return id + mask_account_number(number)
    elif id:
        return id + mask_card_number(number)

    raise ValueError("Не верный формат строки")


def format_date(date: str) -> str:
    """Функция принимает строку с датой в формате: ГГГГ-ММ-ДД чч:мм:сс.мкс
    и возвращает строку с датой в формате: ДД.ММ.ГГГГ"""
    date_obj = datetime.strptime(date[:19], "%Y-%m-%dT%H:%M:%S")

    return date_obj.strftime("%d.%m.%Y")
