from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import get_groups_by_department, add_group

urlpatterns = [
    path('', views.index, name='home'),
    path('registration', views.vusreg, name = 'vusreg'),
    path('add_group/', add_group, name='add_group'),
    path('departments/<int:department_id>/groups/', get_groups_by_department, name='group_list'),

]