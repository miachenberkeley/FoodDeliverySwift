from django.contrib import admin

# Register your models here.
from foodtaskerapp.models import *

admin.site.register(Restaurant)
admin.site.register(Customer)
admin.site.register(Driver)
