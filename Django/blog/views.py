from django.shortcuts import render
from django.http import Http404

from blog.data import posts


# Create your views here.
def blog(request):
    print('blog')

    context = {
        # 'text': 'My blog!',
        'title': 'Blog - ',
        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context,
    )


def post(request, post_id):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404("Post does not exist")

    context = {
        # 'text': 'My blog!',
        'title': 'Blog - ',
        'post': found_post
    }

    return render(
        request,
        'blog/post.html',
        context,
    )