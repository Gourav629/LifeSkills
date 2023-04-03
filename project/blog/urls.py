from django.urls import path
from . import views

urlpatterns = [
    path('',views.Blog),
    path('about/',views.About),
    path('home/',views.Home),
    path('xyz/',views.Xyz),
    path('inter/',views.Interview),
    path('inter_viewer/',views.InterViewers),
]
