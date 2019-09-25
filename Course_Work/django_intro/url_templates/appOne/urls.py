from django.urls import path
from appOne import views

#TEMPLATE TAGGING:
app_name = 'appOne'

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', views.relative, name="relative"),
    path('other/', views.other, name='other'),
]

