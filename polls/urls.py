"""
This Django app is a simple Polls website that allows users to create an account, login and vote on the polls.
The url paths will determine the page the user sees. The default landing page is the login page.
"""
from django.urls import path, include
from . import views
from django.urls import re_path

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    #path('polls/', include('polls.urls')),
]
