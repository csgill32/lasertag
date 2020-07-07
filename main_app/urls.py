from django.urls import path
from . import views

urlpatterns = [
    path('', views.subscribe, name='home'),
    path('adminpage/', views.show_subscribers, name='adminpage')
]