from faker import Faker

faker = Faker(locale="fr_FR")

class payment:

    @staticmethod
    def payment_information():
        return {
            "nameCard": faker.name(),
            "numberCard": faker.credit_card_number(),
            "cvc": faker.credit_card_security_code(),
            "month": faker.month(),
            "year": faker.year()
        }