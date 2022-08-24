from django.urls import path
from products import views

urlpatterns = [
    path('', views.product_list),
    path('<int:pk>', views.product_details),
    path('<int:pk>/update_product_url', views.update_product_url)
]
