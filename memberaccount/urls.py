from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('memberaccount/', views.members_list, name='members_list'),
    path('memberaccount/', views.accounts_balances, name='accounts_balances'),
]