# Django
from django.urls import path, include


urlpatterns = [
    path('user/', include('apps.user.urls')),
    path('top/teachers/', include('apps.main.teacher.urls')),
    path('center/', include('apps.main.center.urls')),
    path('branch/', include('apps.main.branch.urls')),
    path('courses/', include('apps.main.courses.urls')),
]
