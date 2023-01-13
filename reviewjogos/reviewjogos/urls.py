from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from jogos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jogos/', include('jogos.urls')),
    path('', RedirectView.as_view(url='/jogos/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)