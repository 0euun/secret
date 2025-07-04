from django.contrib import admin
from django.urls import path, include
from api.views import login_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='root_login'),
    path('api/', include('api.urls')),
    path('artists/', include('artists.urls')),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
