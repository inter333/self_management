from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view(), name="Index"),
    path('morning', views.CreateMoringView.as_view(),name="CreateMornig"),
    path('night', views.CreateNightView.as_view(),name="CreateNight"),
    #path('home/', views.home, name='home'),
]