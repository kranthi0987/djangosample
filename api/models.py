from django.db import models


# Create your models here.
class Songs(models.Model):
    # song title
    title = models.CharField(max_length=255, null=False)
    # name of artist or group/band
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)


class DummyData(models.Model):
    # title
    title = models.CharField(max_length=255)
    # data
    data = models.IntegerField()
    # image field
    image = models.ImageField(upload_to='media/', default='media/None/no-img.jpg')
