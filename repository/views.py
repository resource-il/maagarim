from django.shortcuts import render
from .models import Repository, Owner
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def repository_index(request):
    repository_list = Repository.objects.all()
    paginator = Paginator(repository_list, 10)

    page = request.GET.get('page')
    try:
        repositories = paginator.page(page)
    except PageNotAnInteger:
        repositories = paginator.page(1)
    except EmptyPage:
        repositories = paginator.page(paginator.num_pages)
    return render(request, 'repository/index.html', {"repositories": repositories})


def repository_view(request, repository_id):
    context = {
        "repository": Repository.objects.get(id=repository_id)
    }
    return render(request, 'repository/view.html', context)


def owner_index(request):
    owner_list = Owner.objects.all()
    paginator = Paginator(owner_list, 10)

    page = request.GET.get('page')
    try:
        owners = paginator.page(page)
    except PageNotAnInteger:
        owners = paginator.page(1)
    except EmptyPage:
        owners = paginator.page(paginator.num_pages)
    return render(request, 'owner/index.html', {"owners": owners})


def owner_view(request, owner_id):
    owner = Owner.objects.get(id=owner_id)

    repository_list = Repository.objects.filter(owner_id=owner_id)
    repo_page = request.GET.get('repo_page')
    repo_paginator = Paginator(repository_list, 10)
    try:
        repositories = repo_paginator.page(repo_page)
    except PageNotAnInteger:
        repositories = repo_paginator.page(1)
    except EmptyPage:
        repositories = repo_paginator.page(repo_paginator.num_pages)

    suggested_list = Repository.objects.filter(owner_name=owner.name).exclude(owner_id=owner_id)
    repo_sugg_page = request.GET.get('repo_sugg_page')
    repo_sugg_paginator = Paginator(suggested_list, 10)
    try:
        suggestions = repo_sugg_paginator.page(repo_sugg_page)
    except PageNotAnInteger:
        suggestions = repo_sugg_paginator.page(1)
    except EmptyPage:
        suggestions = repo_sugg_paginator.page(repo_sugg_paginator.num_pages)

    context = {
        "owner": owner,
        "repositories": repositories,
        "suggestions": suggestions,
    }
    return render(request, 'owner/view.html', context)
