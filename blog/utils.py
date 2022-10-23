from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def pagination(request, newblogs):
    blogs = newblogs
    paginator = Paginator(blogs, 4)
    page = request.GET.get('page1')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    index1 = blogs.number - 1
    max_index1 = len(paginator.page_range)
    start_index1 = index1 - 3 if index1 >= 3 else 0
    end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
    page_range1 = paginator.page_range[start_index1:end_index1]

    return page_range1


def oldPagonation(request, oldBlogs):
    blogs = oldBlogs
    paginator = Paginator(blogs, 4)
    page = request.GET.get('page1')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    index1 = blogs.number - 1
    max_index1 = len(paginator.page_range)
    start_index1 = index1 - 3 if index1 >= 3 else 0
    end_index1 = index1 + 3 if index1 <= max_index1 else max_index1
    page_range2 = paginator.page_range[start_index1:end_index1]

    return page_range2