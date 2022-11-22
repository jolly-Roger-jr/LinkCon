from django.urls import path
from . import views, convert

urlpatterns = [
    path('', views.index, name='home'),
    path('list', views.list, name='list'),
    path('link/<slug:shortlink_url>/', views.link, name='link'),
    path('convert', convert.convert, name='convert'),
    path('login', views.MyProjectLoginView.as_view(), name='login_page'),
    path('register', views.RegisterUserView.as_view(), name='register_page'),
    path('logout', views.MyProjectLogoutView.as_view(), name='logout_page')
]