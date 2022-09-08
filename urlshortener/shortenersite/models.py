from django.db import models

from .utils import create_shortened_url


class Urls(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)
    pub_date = models.DateTimeField(auto_now=True)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = create_shortened_url(self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.long_url} to {self.short_url}'
