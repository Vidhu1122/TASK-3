from django.urls import path
from .views import dashboard_view, home_view, register_view

from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('home/', home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('payment/<int:course_id>/', views.dummy_payment_view, name='dummy_payment'),


]
 