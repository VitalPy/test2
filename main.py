def deb_card(card_num: str):
    if type (card_num) == str and card_num.isdigit() and len(card_num)==16:
        return f'Номер вашей карты катрты : **** **** **** {card_num[-4:]}'
    else:
        return ValueError
print(deb_card(input('')))

