from django.db import models


# Create your models here.

class TableWallpaperUpload(models.Model):
    # title
    title = models.CharField(max_length=255)
    # image field
    image = models.ImageField(upload_to='media/wallpapers/', default='media/wallpaper/None/no-img.jpg')
    thumbnail = models.ImageField(upload_to='media/thumbs/', default='media/wallpaper/None/no-img.jpg')
    category_id = models.IntegerField()
    image_date = models.DateTimeField()
    wallpaper_tags = models.CharField(max_length=500)
    total_rating = models.CharField(max_length=500)
    wallpaper_rating_average = models.CharField(max_length=500)
    wallpaper_total_views = models.IntegerField()
    wallpaper_total_downloads = models.IntegerField()

    def __str__(self):
        return self.title


class TableRating(models.Model):
    post_id = models.IntegerField()
    user_id = models.IntegerField()
    ip_address = models.IntegerField()
    rating = models.IntegerField()
    dateandtime_rating = models.DateTimeField()


class TableCategory(models.Model):
    category_id = models.IntegerField()
    category_name = models.CharField(max_length=500)
    category_image = models.ImageField(upload_to='media/category', default='')
    category_status = models.CharField(max_length=250)
