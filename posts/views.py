from django.shortcuts import render, redirect

from posts.models import Post

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
    pass
    # return redirect('posts.views.get', cat='t', lang=None, mode='t')

def get(request, lang, mode, cat):
    if cat not in "tvb" or mode not in "tn" or not lang:
        return redirect('index')
    posts = Post.objects.filter(cat=cat, lang__name=lang)
    if mode == "t":
        posts = posts.order_by('votes')
    if mode == "n":
        posts = posts.order_by('-pub_date')
    context = {'posts': posts, 'cat': cat, 'lang': lang, 'mode': mode}
    return render(request, 'list.html', context)

def post(request):
    # TODO add posting functionalitu
    pass

