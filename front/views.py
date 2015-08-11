from django.shortcuts import render
from django.http import HttpResponseNotFound
from repository.models import Repository, Owner
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def home(request):
    return render(request, 'front/home.html')


def search(request):
    query = request.POST.get('q')
    if query is None or query is '':
        query = request.GET.get('q')
    if query is None or query is '':
        return HttpResponseNotFound()

    repository_list = Repository.objects.filter(Q(name__icontains=query) | Q(owner__name__icontains=query))

    paginator = Paginator(repository_list, 10)

    page = request.GET.get('page')
    try:
        repositories = paginator.page(page)
    except PageNotAnInteger:
        repositories = paginator.page(1)
    except EmptyPage:
        repositories = paginator.page(paginator.num_pages)
    return render(request, 'front/search.html', {"repositories": repositories, "q": query})
