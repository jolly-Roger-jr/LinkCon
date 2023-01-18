from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login', views.login_user, name='login_page'),
    path('admin', views.RegisterView.as_view(), name='register_page'),
    path('logout', views.logout_user, name='logout_page'),

]