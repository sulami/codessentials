from django.shortcuts import render, redirect

from posts.models import Language, Post

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
    langs = Language.objects.all().order_by('name')
    return render(request, 'index.html', {'langs': langs})

def get(request, lang, cat, mode):
    if cat not in "tvb" or mode not in "tn" or not lang:
        return redirect('posts:index')
    posts = Post.objects.filter(lang__name=lang)
    if cat:
        posts = posts.filter(cat=cat)
    if mode == "t":
        posts = posts.order_by('votes')
    if mode == "n":
        posts = posts.order_by('-pub_date')
    context = {'posts': posts, 'cat': cat, 'lang': lang, 'mode': mode}
    return render(request, 'list.html', context)

def submit(request):
    # TODO add posting functionalitu
    pass

