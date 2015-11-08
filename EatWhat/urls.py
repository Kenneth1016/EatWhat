from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import login, index, logout, register
from restaurants.views import order, follow, followDetail, saveOrderDetail, cancelOrderDetail
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'EatWhat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout),
    url(r'^index/$', index),
    url(r'^accounts/register/$', register),
    url(r'^order/$', order),
    url(r'^follow/$', follow),
    url(r'^followDetail/(\d{1,5})/$', followDetail),
    url(r'^saveOrderDetail/$', saveOrderDetail),
    url(r'^cancelOrderDetail/$', cancelOrderDetail)
)
