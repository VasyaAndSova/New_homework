def get_mask_card(numbers: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    mask_card = f"{numbers[0:4]} {numbers[4:6]}** **** {numbers[12:]}"
    return mask_card


def get_mask_account(numbers: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    mask_account = f"**{numbers[-4:]}"
    return mask_account
