"""
URL configuration for MyWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import view1
from app1.views.view2 import TopicListView, submit_topic, TopicDetailView, add_comment

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index/', view1.index),
    path('list/', view1.list),
    path('add/', view1.add),
    path('login/', view1.login),
    path('logout/', view1.logout),
    path('luli/', view1.cc),
    path('king/', view1.king),
    path('home/', view1.home),
    path('register/', view1.register),
##################################################
    path('submit_topic/', submit_topic, name='submit_topic'),
    path('topic_list/', TopicListView.as_view(), name='topic_list'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='single_topic'),
    path('topic/<int:pk>/', TopicDetailView.as_view(), name='topic_detail'),
    path('add_comment/', add_comment, name='add_comment'),
    path('add_comment/<int:topic_id>/', add_comment, name='add_comment'),

]
