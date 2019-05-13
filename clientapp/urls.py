from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.index, name='index'),
    path('clients/new', views.client_new, name='client_new'),
    path('clients/update/<int:client_id>/', views.client_update, name='client_update'),
]
