from django.db import models

class Language:
    name = models.CharField(max_length=30)

class Post:
    name = models.CharField(max_length=140)
    link = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    language = models.ForeignKey(Language)

