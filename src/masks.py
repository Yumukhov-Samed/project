def get_mask_account(number_card: int) -> str:
    """Функция, которая принимает на вход номер счета и возвращает маску"""
    str_number_card = str(number_card)
    return f"**{str_number_card[-4:]}"


def get_mask_card_number(number_card: int) -> str:
    """Функция, которая принимает на вход номер карты и возвращает её маску"""
    str_number_card = str(number_card)
    return f"{str_number_card[:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"


