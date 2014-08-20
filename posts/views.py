from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from posts.models import Language, Post
from posts.forms import PostForm

from datetime import datetime, timedelta

"""
Categories:
t - text
v - video
b - book

Modes:
t - top
n - new
d - day
w - week
m - month
"""

def index(request):
    langs = Language.objects.all().order_by('name')
    return render(request, 'index.html', {'langs': langs})

def get(request, lang, cat, mode):
    if cat not in "tvb" or mode not in "tndwm" or not lang:
        return redirect('posts:index')
    posts = Post.objects.filter(lang__name=lang)
    if cat:
        posts = posts.filter(cat=cat)
    if mode == "t":
        posts = posts.order_by('-votes')
    if mode == "n":
        posts = posts.order_by('-pub_date')
    if mode == "d":
        posts = posts.filter(pub_date__gte=datetime.now() - timedelta(days=1)
                            ).order_by('-votes')
    if mode == "w":
        posts = posts.filter(pub_date__gte=datetime.now() - timedelta(days=7)
                            ).order_by('-votes')
    if mode == "m":
        posts = posts.filter(pub_date__gte=datetime.now() - timedelta(days=30)
                            ).order_by('-votes')
    page = request.GET.get('p')
    paginator = Paginator(posts, 25)
    try:
        postlist = paginator.page(page)
    except PageNotAnInteger:
        postlist = paginator.page(1)
    except EmptyPage:
        postlist = paginator.page(paginator.num_pages)
    voted = []
    for post in postlist:
        if str(post.pk) in request.COOKIES:
            voted.append(post.pk)
    context = {'posts': postlist, 'voted': voted, 'cat': cat, 'lang': lang,
               'mode': mode}
    return render(request, 'list.html', context)

def upvote(request, id):
    response = HttpResponse()
    if request.is_ajax() and id not in request.COOKIES:
        response.set_cookie(key=id, value=1)
        post = get_object_or_404(Post, pk=id)
        post.votes += 1
        post.save()
    return response

def submit(request):
    if request.method == 'POST':
        post = Post()
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            p = form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    return render(request, 'submit.html', {'form': form})


