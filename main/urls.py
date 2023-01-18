from django.urls import path
from . import views, convert

urlpatterns = [
    path('', views.index, name='home'),
    path('list', views.list, name='list'),
    path('link/<slug:shortlink_url>/', views.link, name='link'),
    path('convert', convert.convert, name='convert'),


]
