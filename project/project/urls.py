from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from blog.views import PostView

route = routers.DefaultRouter()
route.register('', PostView, basename='postview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)