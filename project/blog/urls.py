from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.Index),
    path('home/',views.Home),
    path('temp/',views.Temp),
    path('about/',views.About),
    path('abc/',views.Abc),
    path('xyz/',views.Xyz),
    path('',views.Blog),
]
