from django.contrib import admin
from django.urls import path, include


API_TITLE = 'BLOG_API'
API_DESCRIPTION = 'A web API for creating and editing blog posts.'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
    path('api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    ]
