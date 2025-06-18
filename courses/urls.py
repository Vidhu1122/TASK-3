from django.urls import path
from .views import create_course
from .views import dashboard_view, create_course, course_detail, edit_course, delete_course
from django.urls import path
from .views import course_detail 


urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/create/', create_course, name='create_course'),
    path('edit/<int:course_id>/', edit_course, name='edit_course'),
    path('delete/<int:course_id>/', delete_course, name='delete_course'),
    path('<int:course_id>/', course_detail, name='course_detail'),
]
