from django.urls import path
from blog import views

urlpatterns = [
    path('',views.Blog),
    path('about/',views.About),
    path('home/',views.Home),
    path('xyz',views.Xyz),
    path('inter/',views.Interview),
    path('inter_viewer/',views.IViewers),
    path('volunteer/',views.joinAsVolun),
    path('vol_tra/',views.joinAsTrans),
    path('contact/',views.contact),
]
