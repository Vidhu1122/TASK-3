from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from users.views import home_view
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path('', include('users.urls')),
    path('', include('courses.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard/', include('courses.urls')),
    path('courses/', include('courses.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
