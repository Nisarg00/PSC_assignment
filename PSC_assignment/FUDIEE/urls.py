from django.conf.urls import url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from . import views

urlpatterns = [
    url('index/',views.index,name="fudiee"),
    url('about/', views.about, name="fudiee-about"),
    url('', views.index, name="fudiee-home"),
]

