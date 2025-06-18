from django.urls import path
from .views import home_view, register_view
from .views import dummy_payment_view
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('home/', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('save-progress/<int:course_id>/', views.save_progress, name='save_progress'),
    path('get-progress/<int:course_id>/', views.get_progress, name='get_progress'),
    path('payment/<int:course_id>/', dummy_payment_view, name='dummy_payment'),
]
 