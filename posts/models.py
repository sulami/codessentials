from django.db import models

from urlparse import urlparse

class Language(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

CAT_CHOICES = (
    ("t", "Text"),
    ("v", "Video"),
    ("b", "Book"),
)

class Post(models.Model):
    name = models.CharField(max_length=140)
    link = models.URLField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    lang = models.ForeignKey('Language')
    votes = models.IntegerField(default=0)
    cat = models.CharField(max_length=1, choices=CAT_CHOICES)

    def __unicode__(self):
        return self.name

    def slug(self):
        return urlparse(self.link).hostname

