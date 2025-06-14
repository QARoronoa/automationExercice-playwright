from faker import Faker
from faker.generator import random

faker = Faker(locale="fr-FR")


class Login:
    new_user_signup = [{
        "name": faker.name(),
        "email": faker.email()
    }]

    user_correct_credentials = [{
        "email" : "marguerite20@example.org",
        "password": "Yj4CGAVBY_"
    }]

    register_existing_mail = [{
        "name": faker.name(),
        "email": "marguerite20@example.org"
    }]

    user_incorrect_credentials = [{
        "email": faker.email(),
        "password": faker.password()
    }]

    account_information = [{
        "password": faker.password(),
        "dayBirth": str(random.randint(1, 31)),
        "monthBirth": str(random.randint(1, 12)),
        "yearBirth": faker.year(),
        "firstName": faker.first_name(),
        "lastName": faker.last_name(),
        "adress": faker.address(),
        "state": faker.country(),
        "city": faker.city(),
        "zipCode": "92350",
        "mobileNumer": "876234374"
    }]
