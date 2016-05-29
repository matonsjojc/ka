from django.conf.urls import url
from ka import views

urlpatterns = [
        url(r'^$', views.prva_stran, name="prva_stran"),
]
