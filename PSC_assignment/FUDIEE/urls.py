from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url('index/',views.index,name="fudiee"),
    url('about/', views.about, name="fudiee-about"),
    url('', views.index, name="fudiee-home"),
]
urlpatterns +=  staticfiles_urlpatterns()
