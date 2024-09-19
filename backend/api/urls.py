from django.urls import path
from api import views

urlpatterns=[
    path('product/',views.ProductList.as_view()),
    path('add-to-cart/', views.add_cart_items, name='add-to-cart'),
    # path('insert/',views.data),
]