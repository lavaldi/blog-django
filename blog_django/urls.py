from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from blog import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^blog_django/', include('blog_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'(?P<slug>[^/]+)/$', views.PostView.as_view(), name='post'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
