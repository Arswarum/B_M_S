from tkinter import CASCADE
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

    
class Building(models.Model):
    name = models.CharField(verbose_name='Nazwa', default='', max_length=25, null=False, blank=False)
    pictures = models.ImageField(verbose_name='Zdjęcia',upload_to='static/images/building', null=False, blank=True)
    regulamin = models.FileField(verbose_name='Regulamin', upload_to='static/regulamin', null=False, blank=True)
    info = models.TextField(verbose_name='Informacje', default='', null=False, blank=True)
    building_adres = models.TextField(verbose_name='Adres', default='', null=False, blank=False)
    firm_adres = models.TextField(verbose_name='Adres', default='', null=False, blank=True)
    telefon1 = PhoneNumberField(verbose_name='Telefon', default='', null=False, blank=False)
    telefon2 = PhoneNumberField(verbose_name='Telefon', default='', null=False, blank=True)
    email = models.EmailField(verbose_name='E-mail',  default='', null=False, blank=False)

    def __str__(self):
        return str(self.name)

class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, blank=False)
    name = models.CharField(verbose_name='Segment', default='', max_length=3, null=False, blank=False)
    pictures = models.ImageField(verbose_name='Zdjęcia',upload_to='static/images/segments', null=False, blank=True)
    description = models.TextField(verbose_name='Opis', default='', null=False, blank=True)
    capacity = models.SmallIntegerField(verbose_name='Ilość miejsc', default=5, null=False, blank=False)

    def __str__(self):
        return f"Segment - {self.name}"
    

class Booking(models.Model):
    # Relations
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=CASCADE, blank=True)

    # Date from booking Form partly from User if logedin
    first_name = models.CharField(verbose_name='Imię', default='', max_length=15, null=False, blank=False)
    last_name = models.CharField(verbose_name='Nazwisko', default='', max_length=15, null=False, blank=False)
    email = models.EmailField(verbose_name='E-mail', default='', null=False, blank=False)
    phonenumber = PhoneNumberField(verbose_name='Telefon', default='', blank=False)
    street = models.CharField(verbose_name='Adres', max_length=50, default='', null=False, blank=False)
    zip_code = models.CharField(verbose_name='Kod pocztowy', max_length=6, default='', null=False, blank=False)
    city = models.CharField(verbose_name='Miejscowość', max_length=20, default='', null=False, blank=False)
    adults = models.SmallIntegerField(verbose_name='Liczba dorosłych',default=1, null=False, blank=False)
    childs = models.SmallIntegerField(verbose_name='Liczba dzieci', default=0, null=False, blank=False)
    questions = models.TextField(verbose_name='Zapytania', default='', null=False, blank=True)
    zgoda1 = models.BooleanField(verbose_name=consents[0], default=False, blank=False)
    zgoda2 = models.BooleanField(verbose_name=consents[1], default=False, blank=False)

    checkin = models.DateTimeField()
    checkout = models.DateTimeField()

    status_choices = [
        ('pending','Oczekuję'),
        ('confirmed','Potwirdzona'),
        ('ended','Zakonczona')
    ]
    status = models.CharField(verbose_name='Status', max_length=15, choices=status_choices, default=status_choices[0], null=False, blank=False)


    def __str__(self):
        return f"Segment - {self.room.name} --- {self.first_name} --- {self.last_name} --- {self.email} --- {self.phonenumber} --- {self.city} ---  {self.checkin} --- {self.checkout}"