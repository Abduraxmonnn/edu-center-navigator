# Django
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('apps/', include('apps.urls')),

    path('__debug__/', include('debug_toolbar.urls')),
]

urlpatterns += [
    path(r'i18n/', include('django.conf.urls.i18n')),
    # *i18n_patterns(*urlpatterns, prefix_default_language=False)
]

urlpatterns += tuple(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
urlpatterns += tuple(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
