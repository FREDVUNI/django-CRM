from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path("products",views.products,name="products"),
    path("<str:pk>/customer",views.customers,name="customer"),
    path("<str:pk>/add-order",views.addorder,name="addorder"),
    path("<str:pk>/order",views.updateorder,name="updateorder"),
    path("delete/<str:pk>/order",views.deleteorder,name="deleteorder"),
]