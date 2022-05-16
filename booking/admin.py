from django.contrib import admin
from .models import User, Building, Room, Booking
# Register your models here.

admin.site.register(User)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Booking)