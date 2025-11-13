from django.contrib import admin
from django.urls import path, include
from home import views as home_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('sermons/', home_views.sermon_list_json, name='sermon_list_json'),
    path('sermon_details/<pk>', home_views.sermon_details, name='sermon_details'),

    ]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)