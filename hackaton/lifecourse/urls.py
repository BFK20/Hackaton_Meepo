from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import get_groups_by_department, add_group, getvusprofile

urlpatterns = [
    path('', views.index, name='home'),
    path('vusregistration', views.vusreg, name = 'vusreg'),
    path('add_group/', add_group, name='add_group'),
    path('vuses/<str:vusname>/', getvusprofile, name='group_list'),
    path('createfac/', views.createfac, name='createfuc'),

]