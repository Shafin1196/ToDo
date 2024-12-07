from django.urls import path
from .import views


urlpatterns=[
    path('add/',views.add,name='add'),
    path('',views.list,name='list'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('completePage/',views.completePage,name='completePage'),
    path('complete/<int:pk>/',views.complete,name='complete'),
    path('edit/<int:pk>/',views.edit,name='edit'),

]