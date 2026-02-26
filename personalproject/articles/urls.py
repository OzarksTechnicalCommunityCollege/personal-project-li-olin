from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.articles, name='articles'),
    # path(
    #     '<slug:page>/',
    #      views.Page,
    #      name='page'
    # ),
    path('login/', views.user_login, name='login'),
]