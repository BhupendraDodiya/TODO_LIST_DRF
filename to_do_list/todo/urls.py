from django.urls import path
from todo import views

urlpatterns = [
    path('',views.Homeview,name='home'),
    path('detail/<str:pk>/',views.Detailview,name='detail'),
    path('create/',views.Createview,name='create'),
    path('update/<str:pk>/',views.Updateview,name='update'),
    path('delete/<str:pk>/',views.Deleteview,name='delete'),
]
