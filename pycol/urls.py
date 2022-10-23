from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('conducta', conducta, name='conducta'),
    path('privacy', privacy, name='privacy'),
    
    path('', include('blog.urls')),
    path('', include('eventos.urls')),
    path('', include('comunidad.urls')),

    # path('captcha/', include('captcha.urls')),

    # path('page401', page401, name='page401'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# 401 Unauthorized
# 403 Forbidden
# 404 Not Found
# 415 Unsupported Media Type
# 500 Internal Server Error
# 501 Not Implemented
# 502 Bad Gateway
