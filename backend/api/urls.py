from django.urls import path
from api import views

urlpatterns=[
    path('product/',views.ProductList.as_view()),
    path('add-to-cart/', views.add_cart_items, name='add-to-cart'),
    path('signup/',views.Signup),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
     path('contact/', views.contact_view, name='contact'),
]



    # path('insert/',views.data),