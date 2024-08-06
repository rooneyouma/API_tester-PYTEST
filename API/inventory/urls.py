from django.urls import path
from . import views

urlpatterns = [
    path('api/Item_list/',views.Item_list,),
    path('api/Item_list/<int:id>/',views.Item_detail),
]