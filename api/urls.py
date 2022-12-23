from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="home"),
    path("create/", views.addItem, name="add-item"),
    path("items/", views.getAllItems, name="get-all-items"),
    path("item/<int:id>", views.getItem, name="get-item"),
    path("item/delete/<int:id>", views.deleteItem, name="delete-item"),
    path("item/update/<int:id>", views.updateItem, name="update-item"),
]
