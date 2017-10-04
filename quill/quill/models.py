from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50)
    delta_content = JSONField(blank=True, null=True)
    published = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published = True
