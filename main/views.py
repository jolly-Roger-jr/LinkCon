from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .models import Link
from .forms import LinkForm, AuthUserForm, RegisterUserForm
from django.contrib.auth.models import User
HOST = 'http://127.0.0.1:8000/'


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

class MyProjectLoginView(LoginView):
    template_name = 'main/login.html'
    form_class = AuthUserForm
    success_url = '/'
    def get_success_url(self):
        return self.success_url

class MyProjectLogoutView(LogoutView):
    next_page = '/'

class RegisterUserView(CreateView):
    model = User
    template_name = 'main/register_page.html'
    form_class = RegisterUserForm
    success_url = '/'
    success_msg = 'Пользователь успешно создан'


def list(request):
    links = Link.objects.order_by('id')
    print(links)
    context = {
        'links': links,
        'original_url': 'LinkConv',
        'host': HOST
    }
    return render(request, 'main/list.html', context)


def link(shortlink_url):
    link = Link.objects.filter(shortlink_url=shortlink_url)
    if not link:
        return HttpResponse('Not found')
    original_url = link.first().original_url
    return redirect(original_url)

