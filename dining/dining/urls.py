from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('users.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/login/$', 'django_cas.views.login'),
                       url(r'^accounts/logout/$', 'django_cas.views.logout'),
                       url(r'^favorites/$', 'users.views.favorites'),
)
    # Examples:
    # url(r'^$', 'dining.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)
