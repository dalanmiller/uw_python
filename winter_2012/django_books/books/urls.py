from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'book.views.index', name='index'),
    url(r'^book/(?P<book_id>\d+)', 'book.views.book', name='book'),
    # url(r'^books/', include('books.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
  	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
