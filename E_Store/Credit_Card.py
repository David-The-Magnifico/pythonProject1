from E_Store import Card_Type


class Credit_Card:

    def __init__(self, name_on_card: str, cvv: str, card_expiration_date: str, credit_card_number: str,
                 card_type: Card_Type):
        self.card_expiration_date = card_expiration_date
        self.name_on_card = name_on_card
        if len(cvv) in 3:
            self.cvv = int(cvv)
        else:
            raise ValueError("invalid cvv provided.")
        if credit_card_number.isnumeric() and len(credit_card_number) in (13, 14, 15, 16):
            self.creditCardNumber = credit_card_number
        else:
            raise ValueError("invalid cardNumber")
        self.card_expirationDate = credit_card_number
        self.card_type = card_type