from django.contrib import admin

# Register your models here.
from wallpaperapi.models import TableWallpaperUpload, TableCategory, TableRating

admin.site.register(TableWallpaperUpload)
admin.site.register(TableCategory)
admin.site.register(TableRating)
