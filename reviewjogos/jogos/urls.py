from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='/jogos/')),
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
]