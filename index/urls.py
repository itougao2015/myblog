from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.index),
    path('<str:year>/<int:month>/<slug:day>',views.mydate),
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',views.mydate),
    re_path('(?P<year>[0-9]{4})/',views.myyear,name='myyear')
]