from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from apps.welcome.views import error_404, error_500

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include("apps.welcome.urls")),
    path('service/', include("apps.record.urls")),
    path('users/', include("apps.users.urls", namespace='users')),
    path('__debug__/', include("debug_toolbar.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = error_404
handler500 = error_500