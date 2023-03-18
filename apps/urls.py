# Django
from django.urls import path, include

urlpatterns = [
    path('user/', include('apps.user.urls')),
    path('top/teachers/', include('apps.main.teacher.urls'))
]
