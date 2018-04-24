import random

AFFILIATE_ID = '1111'
BIRTH_DATE = '1990-01-01'
BRAND_ID = 'redbox'
BTAG = "NOTEMPTY"
COUNTRY = 'UA'
CURRENCY = 'EUR'
EMAIL_DOMAIN = "mail.com"
LANGUAGE_CODE = 'UK'
PASSWORD = 'Test123'
PHONE_CODE = '380'
PHONE = '5556677'
TERMS_AND_CONDITION_ID = 'TERMS-1d16b8cb-6e3b-447a-9682-75f048d49285'


class User():
    def __init__(self, email=None):
        self._affiliateId = AFFILIATE_ID
        self._birthDate = BIRTH_DATE
        self._brandId = BRAND_ID
        self._btag = BTAG
        self._country = COUNTRY
        self._currency = CURRENCY
        self._email = self.generate_email() if email is None else self.email
        self._languageCode = LANGUAGE_CODE
        self._password = PASSWORD
        self._phone = PHONE
        self._phoneCode = PHONE_CODE
        self._termsAndConditionsId = TERMS_AND_CONDITION_ID

    @property
    def affiliate_id(self):
        return self._affiliateId

    @property
    def birth_date(self):
        return self._birthDate

    @property
    def brand_id(self):
        return self._brandId

    @property
    def btag(self):
        return self._btag

    @property
    def country(self):
        return self._country

    @property
    def currency(self):
        return self._currency

    @property
    def language_code(self):
        return self._languageCode

    @property
    def password(self):
        return self._password

    @property
    def phone(self):
        return self._phone

    @property
    def phone_code(self):
        return self._phoneCode

    @property
    def termsandcond(self):
        return self._termsAndConditionsId

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = "{}@{}".format(value, EMAIL_DOMAIN)

    def generate_email(self):
        return "{}@{}".format(random.randint(11111, 99999), EMAIL_DOMAIN)
