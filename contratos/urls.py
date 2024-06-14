from django.urls import path
from .import views

urlpatterns = [
  path('', views.index, name='contratos'),
  path('view/<int:id>', views.view, name='contratos_view'),
  path('edit/<int:id>', views.edit, name='contratos_edit'),
  path('create/', views.create, name='contratos_create'),
  path('delete/<int:id>', views.delete, name='contratos_delete')
]