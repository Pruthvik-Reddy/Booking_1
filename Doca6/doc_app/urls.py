from django.conf.urls import url
from doc_app import views

urlpatterns=[

        url(r'^$',views.index,name='index'),


]