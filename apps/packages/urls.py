from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('about', about, name = 'about'),
    path('category_list/', category_list, name = 'category_list'), 
    path('category_create/', category_create, name='category_create'), 
    path('category_update/<id>/', category_update, name='category_update'), 
    path('category_delete/<id>/', category_delete, name='category_delete'), 
    path('classification_list/', classification_list, name = 'classification_list'),  
    path('classification_create/', classification_create, name='classification_create'),   
    path('classification_update/<id>/', classification_update, name='classification_update'),   
    path('classification_delete/<id>/', classification_delete, name='classification_delete'),   
    path('product_list/', product_list, name = 'product_list'),    
    path('product_create/', product_create, name='product_create'),
    path('product_read/<id>/', product_read, name='product_read'),   
    path('product_update/<id>/', product_update, name='product_update'),
    path('product_delete/<id>/', product_delete, name='product_delete'),
    path('product_search/', product_search, name='product_search'),
    path('product_category/', product_category, name='product_category'),
    path('product_classification/', product_classification, name='product_classification'),
]
