from django.db import models

class Language:
    name = models.CharField(max_length=30)

class Post:
    """Base post class to inherit from"""
    name = models.CharField(max_length=140)
    link = models.URLField()
    pub_date = models.DateTimeField(auto_now_add=True)
    lang = models.ForeignKey(Language)
    votes = models.IntegerField()

class TextPost(Post):
    """Link->text post"""
    pass

class VideoPost(Post):
    """Link->video post"""
    pass

class BookPost(Post):
    """Link->book post"""
    pass

