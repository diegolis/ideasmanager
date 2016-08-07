from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^export_year/', export_year),
]
