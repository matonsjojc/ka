from django.conf.urls import url
from ka import views

urlpatterns = [
        url(r'^$', views.user_login, name="login"),
        url(r'^login/$', views.user_login, name="login"),
        url(r'^index/$', views.index, name="index"),
        url(r'^vprasanje/$', views.vprasanje, name="vprasanje"),
]
