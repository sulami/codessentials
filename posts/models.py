from django.db import models

from urlparse import urlparse

class Language(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=140)
    link = models.URLField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    lang = models.ForeignKey('Language')
    votes = models.IntegerField(default=0)
    cat = models.CharField(max_length=1)

    def __str__(self):
        return self.name

    def slug(self):
        return urlparse(self.link).hostname

