from django.contrib import admin

# Register your models here.
from account.models import UserProfileInfo

admin.site.register(UserProfileInfo)
