from  django.urls  import  path
from  .  import  views
app_name='cart'
urlpatterns=[
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('/a',views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('delete/<int:product_id>/', views.cart_delete, name='cart_delete'),
    path('cart_payment/', views.cart_payment, name='cart_payment'),
]