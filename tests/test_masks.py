from src.masks import get_mask_account, get_mask_card


def test_get_mask_card(numbers_card):
    assert get_mask_card(numbers_card) == "7000 79** **** 6361"


def test_get_mask_account(numbers_account):
    assert get_mask_account(numbers_account) == "**4305"
