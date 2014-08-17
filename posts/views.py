from django.shortcuts import render, redirect

from posts.models import TextPost, VideoPost, BookPost

"""
Categories:
t - text
v - video
b - book

Modes:
t - top
n - new
"""

def index(request):
    return redirect('get', 't', None, 't')

def get(request, cat, language, mode):
    if cat not in "tvb" or mode not in "tn":
        return redirect('index')
    if cat == "t":
        posts = TextPost.objects.all()
    if cat == "v":
        posts = VideoPost.objects.all()
    if cat == "b":
        posts = BookPost.objects.all()
    if language:
        posts = posts.get(lang=language)
    if mode == "t":
        posts = posts.order_by('votes')
    if mode == "n":
        posts = posts.order_by('-pub_date')
    context = {'posts': posts, 'cat': cat, 'lang': language, 'mode': mode}
    return render('sometemplate.html', context)

def post(request):
    # TODO add posting functionalitu
    pass

