from django.urls import path
from . import views

urlpatterns= [
    path('',views.item_list),
    path('item/<int:pk>',views.item_detail),
]

