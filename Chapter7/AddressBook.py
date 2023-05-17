from faker import Faker
from faker.providers import person, job, company, internet


class BusinessCard:
    def __init__(self, name, family_name, company_name, position, e_mail):
        self.name = name
        self.family_name = family_name
        self.company_name = company_name
        self.position = position
        self.e_mail = e_mail

    def __str__(self):
        return 'Name:' + self.name + '; Family Name:' + self.family_name + '; Company Name:' + self.company_name + \
            '; Position:' + self.position + '; E-mail:' + self.e_mail


fake = Faker()
fake.add_provider(person)
fake.add_provider(job)
fake.add_provider(company)
fake.add_provider(internet)

business_cards_list = []

for i in range(5):
    business_card = BusinessCard(fake.first_name_male(), fake.last_name_male(), fake.company(), fake.job(),
                                 fake.company_email())
    business_cards_list.append(business_card)
    print(business_card)
#print(business_cards_list)