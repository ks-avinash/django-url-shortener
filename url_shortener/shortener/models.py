from django.db import models


class ShortURL(models.Model):
    url = models.URLField(max_length=200)
    unique_id = models.SlugField(max_length=6, primary_key=True, blank=True)
    count = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now=True)
    shortened_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return str(self.url)
