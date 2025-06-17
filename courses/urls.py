from django.urls import path
from .views import create_course
from .views import dashboard_view, create_course, course_detail
from django.urls import path
from .views import course_detail 


urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard/create/', create_course, name='create_course'),
    path('<int:course_id>/', course_detail, name='course_detail'),
]
