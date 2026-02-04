from django.urls import path
from . import views

urlpatterns = [
    path('', views.Page, name='page'),
    path(
        '<slug:post>/',
         views.Page,
         name='page'
    ),
]