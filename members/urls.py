from django.urls import path
from . import views
urlpatterns = [
    path('members/',views.all_members,name='members'),
    path('members/details/<int:id>', views.details,name='details'),
    path('',views.main,name='home'),
    path('testing/',views.testing,name='testing'),
]  
