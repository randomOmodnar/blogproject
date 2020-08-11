from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# def index(request):
#     return HttpResponse('welcome to my blog!')

# def index(request):
#     return render(request,'blog/index.html',context={
#         'title':'Home page of my blog',
#         'welcome':'Welcome to my blog',
#     })

app_name = 'blog'
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={
        'post_list':post_list,
        # 'static':'blog/static'
    })

def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={
        'post':post,
    })
