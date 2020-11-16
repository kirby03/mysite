from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def index(request):
    #blogs = get_object_or_404(Blog, pk=blog_id)
    #context = {'blogs': blogs,}
    latest_blog_list = Blog.objects.order_by('-pub_date')[:5]
    context = {'latest_blog_list': latest_blog_list,}
    return render(request, 'new_blog/index.html', context)