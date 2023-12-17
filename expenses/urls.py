from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_expense, name='view_expense'),
    # path('toggle_status/<int:id>', views.toggle_status, name='toggle_status'),
    path('toggle/<int:id>', views.toggle, name='toggle'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
]