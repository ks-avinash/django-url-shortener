from django.db import models
# Create your models here.


class ShortURL(models.Model):
    url = models.CharField(max_length=200)
    unique_id = models.SlugField(max_length=6, primary_key=True, blank=True)
    count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.url)