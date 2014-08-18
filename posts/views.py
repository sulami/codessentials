from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from posts.models import Language, Post
from posts.forms import PostForm

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
    page = request.GET.get('p')
    paginator = Paginator(posts, 25)
    try:
        postlist = paginator.page(page)
    except PageNotAnInteger:
        postlist = paginator.page(1)
    except EmptyPage:
        postlist = paginator.page(paginator.num_pages)
    context = {'posts': postlist, 'cat': cat, 'lang': lang, 'mode': mode}
    return render(request, 'list.html', context)

def submit(request):
    if request.method == 'POST':
        post = Post()
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            p = form.save()
            # messages.success(request, project_started)
            return redirect('posts:index', project.pk)
    else:
        form = PostForm()
    return render(request, 'submit.html', {'form': form})


