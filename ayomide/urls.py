from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django. conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', include('contact.urls')),
    path("unicorn/", include("django_unicorn.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)