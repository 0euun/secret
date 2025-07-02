from django.contrib import admin
from django.urls import path, include
from api.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='root_login'),
    path('api/', include('api.urls')),
    path('artists/', include('artists.urls')),
]
