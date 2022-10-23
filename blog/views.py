from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
from datetime import datetime, timedelta
from .forms import CommentForm
from .utils import *
from .models import *


# def blog(request):
#     newblogs = []
#     oldBlogs = []
#     today = timezone.now()
#     dia_delta = timedelta(days=30)
    
#     blogs = Post.objects.all().order_by('-date_add')      #[:8] at end for last 8 records
#     for record in blogs:
#         diferencia = today - record.date_add
        

#         if diferencia > dia_delta:
#             oldBlogs.append(record)
#         else:
#             newblogs.append(record)

#     page_range1 = pagination(request, newblogs)
#     page_range2 = oldPagonation(request, oldBlogs)
    
#     context = {'title': 'Blog', 'newblogs':newblogs, 'oldBlogs':oldBlogs, "blogs": blogs, 'page_range1': page_range1, 'page_range2': page_range2}
#     return render(request, 'blog/blog.html', context)


def blogDetail(request, slug):
    blog = Post.objects.get(slug=slug)
    oldBlogs = Post.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogDetail', slug=slug)
    else:
        form = CommentForm()

    context = {'title': 'Blog Detail', 'blog':blog, 'oldBlogs':oldBlogs, 'form':form}
    return render(request, 'blog/blog_detail.html', context)



def blog(request):
    newblogs = []
    oldBlogs = []
    today = timezone.now()
    dia_delta = timedelta(days=30)
    
    blogs = Post.objects.all().order_by('-date_add')      #[:8] at end for last 8 records
    for record in blogs:
        diferencia = today - record.date_add

        if diferencia > dia_delta:
            oldBlogs.append(record)
        else:
            newblogs.append(record)


    paginator = Paginator(newblogs, 4)
    page = request.GET.get('page1')
    try:
        newblogs = paginator.page(page)
    except PageNotAnInteger:
        newblogs = paginator.page(1)
    except EmptyPage:
        newblogs = paginator.page(paginator.num_pages)
    index1 = newblogs.number - 1
    max_index1 = len(paginator.page_range)
    start_index1 = index1 - 3 if index1 >= 3 else 0
    end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
    page_range1 = paginator.page_range[start_index1:end_index1]

    if oldBlogs:
        paginator = Paginator(oldBlogs, 4)
        page = request.GET.get('page1')
        try:
            oldBlogs = paginator.page(page)
        except PageNotAnInteger:
            oldBlogs = paginator.page(1)
        except EmptyPage:
            oldBlogs = paginator.page(paginator.num_pages)
        index1 = oldBlogs.number - 1
        max_index1 = len(paginator.page_range)
        start_index1 = index1 - 3 if index1 >= 3 else 0
        end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
        page_range2 = paginator.page_range[start_index1:end_index1]
    else:
        page_range2 = 0


    context = {'title': 'Blog', 'newblogs':newblogs, 'oldBlogs':oldBlogs, "blogs": blogs, 'page_range1': page_range1, 'page_range2': page_range2}
    return render(request, 'blog/blog.html', context)


