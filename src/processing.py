from typing import Any


def get_dict_by_key_state(list_dict: list[dict[str, object]], key_state: str = "EXECUTED") -> list[dict[str, object]]:
    """Функция возвращает список тех словарей, у которых ключ state содержит переданное в функцию значение"""
    new_list_dict = []
    for dicts in list_dict:
        if dicts["state"] == key_state:
            new_list_dict.append(dicts)
    return new_list_dict


def get_dict_date_dicrease(list_dict: Any, sorting_order: bool = True) -> list[dict[str, object]]:
    """Функция возвращает список словарей отсортированных по убыванию даты"""
    if sorting_order is True:
        new_list_dict = sorted(list_dict, key=lambda dicts: dicts["date"], reverse=sorting_order)
        return new_list_dict
    else:
        new_list_dict = sorted(list_dict, key=lambda dicts: dicts["date"])
        return new_list_dict
