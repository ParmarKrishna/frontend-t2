from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('base.html',views.home,name="base"),
    path('apply',views.apply,name="Apply-Leave"),
    path('eview.html',views.eview,name="Employee-View"),
    path('resign.html',views.resign,name="Resign"),
    path('add.html',views.add,name="Add-Employee"),
    path('query',views.query,name="query")
]