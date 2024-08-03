import logging
import os

# Созание логеров для mask_card_number и mask_account_number
mc_logger = logging.getLogger("mask_card_number")
ma_logger = logging.getLogger("mask_account_number")
# Создание хендлеров для mc_logger и mа_logger
mc_file_handler = logging.FileHandler(os.path.join("logs", "mask_card_number.log"), "w")
ma_file_handler = logging.FileHandler(os.path.join("logs", "mask_account_number.log"), "w")
# Создание форматера
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s")
# Установка форматера для хендлеров
mc_file_handler.setFormatter(file_formatter)
ma_file_handler.setFormatter(file_formatter)
# Добавление хендлеров к соответствующим логерам
mc_logger.addHandler(mc_file_handler)
ma_logger.addHandler(ma_file_handler)
# Настройка уровней логирования
mc_logger.setLevel(logging.DEBUG)
ma_logger.setLevel(logging.DEBUG)


def mask_card_number(number: str) -> str:
    """Функция принимает строку с номером карты и возвращает ее в формате:
    XXXX XX** **** XXXX"""
    mc_logger.info("Проверка корректности входных данных")
    if type(number) is not str:
        mc_logger.error("Неверный тип данных, ожидается строка")
        raise TypeError("Ожидается строка")
    if not number.isdigit() or len(number) != 16:
        mc_logger.error("Неверное значение, должно быть 16 цифр")
        raise ValueError("Должно быть только 16 цифр")
    mc_logger.info("Проверка входных данных успешно завершена")

    mc_logger.info("Начало маскировки номера")
    mask_number = number[:6] + "*" * 6 + number[-4:]
    mc_logger.info(f"Результат маскировки: {mask_number}")

    mc_logger.info("Начало форматирования номера на блоки")
    format_number = " ".join([mask_number[i: i + 4] for i in range(0, 16, 4)])
    mc_logger.info(f"Результат форматирования: {format_number}")

    mc_logger.info("Завершение программы")
    return format_number


def mask_account_number(number: str) -> str:
    """Функция принимает строку с номером счета и возвращает ее в формате: **XXXX"""
    ma_logger.info("Проверка корректности входных данных")
    if type(number) is not str:
        ma_logger.error("Неверный тип данных, ожидается строка")
        raise TypeError("Ожидается строка")
    if not number.isdigit() or len(number) != 20:
        ma_logger.error("Неверное значение, должно быть 20 цифр")
        raise ValueError("Должно быть только 20 цифр")
    ma_logger.info("Проверка входных данных успешно завершена")

    ma_logger.info("Начало форматирования номера счета")
    result = "**" + number[-4:]
    ma_logger.info(f"Результат форматирования: {result}")

    ma_logger.info("Завершение программы")
    return result
