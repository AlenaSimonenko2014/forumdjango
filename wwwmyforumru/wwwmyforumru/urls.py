from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from registration.forms import RegistrationFormUniqueEmail

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'', include('forum.urls', namespace='forum')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
    )