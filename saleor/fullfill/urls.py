from django.conf.urls import url

from . import views

urlpatterns = [url(r"^(\d+)/pay$", views.fullfill, name="fullfill"), url(r"^(\d+)$", views.getInfo, name="getInfo")]
