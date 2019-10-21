from django.contrib import admin
from .models import Songs, DummyData

# Register your models here.

admin.site.register(Songs)
admin.site.register(DummyData)
