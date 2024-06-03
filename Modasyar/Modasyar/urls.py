from django.contrib import admin
from django.urls import path,include
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("myApp.urls")),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)