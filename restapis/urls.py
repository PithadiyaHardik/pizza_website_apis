from django.urls import path
from . import views

urlpatterns = [
    path('store_pizza', views.store_pizza, name="store_pizza"),
    path('show_all',views.show_all.as_view()),
    path('update_pizza/<int:id>',views.update_pizza.as_view()),
    path('delete_pizza/<int:id>',views.delete_pizza.as_view()),
    path('add_order',views.add_order),
]
