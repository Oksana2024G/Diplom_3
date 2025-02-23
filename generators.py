from faker import Faker
import random

class Person:
    faker = Faker()

    @classmethod
    def generate_user_body(cls):
        name = cls.faker.first_name()
        email = f"{name}{cls.faker.last_name().lower()}{random.randint(1, 999)}@yandex.ru"
        password = cls.faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
        return {"email": email,
                "password": password,
                "name": name
                }
