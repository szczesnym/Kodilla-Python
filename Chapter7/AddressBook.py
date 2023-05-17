from faker import Faker
from faker.providers import person, job, company, internet


class BusinessCard:
    def __init__(self, name, family_name, company_name, position, e_mail):
        self.name = name
        self.family_name = family_name
        self.company_name = company_name
        self.position = position
        self.e_mail = e_mail
        self._length = len(self.name) + len(self.family_name) + 1

    def __str__(self):
        return 'Name:' + self.name + '; Family Name:' + self.family_name + '; E-mail:' + self.e_mail
        # return 'Name:' + self.name + '; Family Name:' + self.family_name + '; Company Name:' + self.company_name + \
        #    '; Position:' + self.position + '; E-mail:' + self.e_mail

    def contacts(self):
        print(f'Please contact with: {self.name} {self.family_name} email:{self.e_mail}')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value != len(self.name) + len(self.family_name) + 1:
            raise ValueError(f' Value {value} not eq to len of name and family name')
        else:
            self._length = value


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
    # print(business_card)
# print(business_cards_list)
cards_by_name = sorted(business_cards_list, key=lambda card: card.name)
cards_by_family_name = sorted(business_cards_list, key=lambda card: card.family_name)
cards_by_email = sorted(business_cards_list, key=lambda card: card.e_mail)

for card in cards_by_email:
    print(card.contacts())
    print(card.length)
