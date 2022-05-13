from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

consents = [
    'Wyrażam zgodę na otrymanie na podany przeze mnie w formularzu adres e-mail oraz numer telefonu informacji w zakresie związanym ze zlożona rezerwacje przeze mnie',
    'Zapoznałem się z Regulaminem i akceptuję jego postanowienia'
]

class User(AbstractUser):
    username =  models.CharField(verbose_name='Username', default='',max_length=15, null=False, blank=False)
    first_name = models.CharField(verbose_name='Imię', default='', max_length=15, null=False, blank=False)
    last_name = models.CharField(verbose_name='Nazwisko', default='', max_length=15, null=False, blank=False)
    email = models.EmailField(verbose_name='E-mail', default='', null=False, blank=False, unique=True)
    phonenumber = PhoneNumberField(verbose_name='Telefon', default='', blank=False)
    street = models.CharField(verbose_name='Adres', max_length=50, default='', null=False, blank=False)
    zip_code = models.CharField(verbose_name='Kod pocztowy', max_length=6, default='', null=False, blank=False)
    city = models.CharField(verbose_name='Miejscowość', max_length=20, default='', null=False, blank=False)
    zgoda1 = models.BooleanField(verbose_name=consents[0], default=False, blank=False)
    zgoda2 = models.BooleanField(verbose_name=consents[1], default=False, blank=False)

    USERNAME_FIELD  = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name} --- {self.email} --- {self.phonenumber} --- {self.city}"

    

