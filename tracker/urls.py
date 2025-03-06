from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_transaction, name='add_transaction'),
    path('reset/', views.reset_transactions, name='reset_transactions'),  # New URL for reset

]