from src.masks import get_mask_account, get_mask_card


def get_mask_card_or_account(numbers: str) -> str:
    """Функция принимает тип карты/счета и номер карты/счета и возращает их маску"""
    if "Счет" in numbers:
        mask_account = get_mask_account(numbers.split()[-1])
        result = f"{numbers[:-20]}{mask_account}"
        return result
    else:
        mask_card = get_mask_card(numbers.split()[-1])
        result = f"{numbers[:-16]}{mask_card}"
        return result


def get_date_string(date: str) -> str:
    """Функция принимает строку и возвращает строку с датой"""
    date_string = date[:10].split("-")[::-1]
    return ".".join(date_string)
