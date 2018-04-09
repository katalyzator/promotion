from django.conf.urls import url, include

from main.views import get_user_detail

urlpatterns = [
    url(r'^get_user_detail/$', get_user_detail, name='get_user_detail')
]

