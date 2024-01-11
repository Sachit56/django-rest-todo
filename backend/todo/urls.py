from django.urls import path
from . import views

app_name='todo'

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('create/',views.CreateView.as_view(),name='home'),
    path('delete/<int:pk>/',views.DeleteView.as_view(),name='home'),



]
