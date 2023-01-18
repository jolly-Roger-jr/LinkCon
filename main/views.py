from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Link
from .forms import LinkForm

HOST = 'http://127.0.0.1:8080/'


def index(request):
    error = ''
    value1 = ''
    link_form = LinkForm()
    context = {
        'link': link_form,
        'shortlink_url': value1,
        'error': error
    }

    return render(request, 'main/index.html', context)


def list(request):
    links = Link.objects.order_by('id')
    print(links)
    context = {
        'links': links,
        'original_url': 'LinkConv',
        'host': HOST
    }
    return render(request, 'main/list.html', context)


def link(request, shortlink_url):
    link = Link.objects.filter(shortlink_url=shortlink_url)
    if not link:
        return HttpResponse('Not found')
    original_url = link.first().original_url
    return redirect(original_url)

