
from django.contrib import admin
from django.urls import path, include

from ecommerceapp import views
app_name='ecommerceapp'

urlpatterns = [
  path('',views.allProdcat, name='allProdcat'),
  path('<slug:c_slug>/',views.allProdcat,name='products_by_category'),
  path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name='prodcatdetail'),
]
