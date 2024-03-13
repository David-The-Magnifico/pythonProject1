from E_Store import Address
from E_Store import Card_Type
from E_Store import Credit_Card
from E_Store import Customer


def test_forCustomer_AddBillingInfofmationAndBillingInformationIsAdded(self):
    home_address = Address("15", "Gbajabiamila street", "Surulere", "Lagos", "Nagiria")
    customer = Customer("David Oladipo", 24, home_address, "Fortune500@gmail.com", "Unicorn")
    delivery_address = Address("15", "Gbajabiamila street", "Surulere", "Lagos", "Nagiria")
    card = Credit_Card("David ", "579", "03/30", "4538976549016", Card_Type.MASTERCARD)
    customer.add_billling_info("Elon Musk", "67894538", delivery_address, card)
    assert customer.get_number_of_billing_info() == 1