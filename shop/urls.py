from django.urls import path
from . import views


urlpatterns = [
    path('products', views.index, name="products"),
    path('', views.prod, name=""),
    path('show', views.show, name="show"),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]

