from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_course_view, name='create_course'),
    path('<int:course_id>/', views.course_detail_view, name='course_detail'),
]

# This file defines the URL patterns for the courses app.
# It includes a single URL pattern that maps to the course detail view. 