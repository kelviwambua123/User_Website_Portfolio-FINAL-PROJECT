from django.urls import path
from . import views
from portfolio.views import project_list

urlpatterns = [
    path('', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('project_list/', project_list, name='project_list'),
]