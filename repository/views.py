from django.shortcuts import render
from .models import Repository
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
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


def view(request, repository_id):
    context = {
        "repository": Repository.objects.get(id=repository_id)
    }
    return render(request, 'repository/view.html', context)
