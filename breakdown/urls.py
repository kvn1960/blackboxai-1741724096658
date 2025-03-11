from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('breakdowns/', views.BreakdownListView.as_view(), name='breakdown_list'),
    path('breakdowns/new/', views.BreakdownCreateView.as_view(), name='breakdown_create'),
    path('breakdowns/<int:pk>/', views.BreakdownDetailView.as_view(), name='breakdown_detail'),
    path('breakdowns/<int:pk>/edit/', views.BreakdownUpdateView.as_view(), name='breakdown_update'),
    path('breakdowns/<int:pk>/delete/', views.BreakdownDeleteView.as_view(), name='breakdown_delete'),
]
