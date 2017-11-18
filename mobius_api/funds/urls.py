from django.conf.urls import url
from funds import views

urlpatterns = [
    url(r'^home/$', views.Home.as_view(), name='home'),
]