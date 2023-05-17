from faker import Faker
from faker.providers import person, job, company, internet, phone_number


class BaseCard:
    def __init__(self, name, family_name, e_mail, priv_phone):
        self.name = name
        self.family_name = family_name
        self.e_mail = e_mail
        self.priv_phone = priv_phone
        self._length = len(self.name) + len(self.family_name)

    def __str__(self):
        return 'Name:' + self.name + '; Family Name:' + self.family_name + '; E-mail:' + self.e_mail + \
            '; Phone:' + self.priv_phone

    def contacts(self):
        print(f'Please contact with: {self.name} {self.family_name} private phone:{self.priv_phone}')

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value != len(self.name) + len(self.family_name) + 1:
            raise ValueError(f' Value {value} not eq to len of name and family name')
        else:
            self._length = value


class BusinessCard(BaseCard):
    def __init__(self, position, company, business_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone

    def contacts(self):
        print(f'Please contact with: {self.name} {self.family_name} corporate phone:{self.business_phone}')

    def __str__(self):
        return super().__str__() + '; Position:' + self.position + ' ;Company:' + self.company + \
            ' ;Buss Phone:' + self.business_phone + ' ;LEN:' + str(self._length)


def create_contacts(type='Base', quantity=1):
    fake = Faker()
    fake.add_provider(person)
    fake.add_provider(job)
    fake.add_provider(internet)
    list_of_cards = []
    if type == 'Base':
        for i in range(quantity):
            card = BaseCard(name=fake.first_name_male(), family_name=fake.last_name_male(),
                            e_mail=fake.company_email(), priv_phone=fake.phone_number())
            list_of_cards.append(card)
    elif type == 'Business':
        fake.add_provider(company)
        for i in range(quantity):
            card = BusinessCard(name=fake.first_name_male(), family_name=fake.last_name_male(),
                                e_mail=fake.company_email(), priv_phone=fake.phone_number(), position=fake.job(),
                                company=fake.company(), business_phone=fake.phone_number())
            list_of_cards.append(card)
    else:
        ValueError('fWrong card type provided - Base or Business')
    return list_of_cards


cards = create_contacts(type='Business', quantity=10)
for card in cards:
    print(card)
