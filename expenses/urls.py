from django.urls import path
from .views import ExpenseList, ExpenseDetail


urlpatterns = [
    path('expenses/', ExpenseList.as_view(), name='expense-list'),
    path('expenses/<str:category>/', ExpenseList.as_view(), name='category-expense-list'),
    path('expenses/<int:expense_id>/', ExpenseDetail.as_view(), name='expense-detail'),
]
