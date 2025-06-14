from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_course, name='create_course'),
    path('', views.course_list, name='course_list'),
]
# The above code defines URL patterns for the courses app in a Django project.
# It includes a path for creating a course and a path for listing all courses.  