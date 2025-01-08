from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/<str:unique_id>/', views.dashboard, name='dashboard'),
    path('edit/', views.edit_card, name='edit_card'),
]
