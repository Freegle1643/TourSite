from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^$',home),
    url(r'^home/$',home),
    url(r'^login/$',loginpage),
    url(r'^register/$',registerpage),
    url(r'^logout/$',logoutfunction),
    url(r'^destination(?P<destid>\d+)/$',destination),
    url(r'^forum/$',forum),
    url(r'^triplist/$',triplist),
    url(r'^trip(?P<tripid>\d+)/$',trip),
    url(r'^journal(?P<jjid>\d+)/$',journal),
    url(r'^editjournal/$',editjournal),
    url(r'^addjournal/$',addjournal),
    url(r'^personal/$',personal),
    url(r'^profile/$',profile),
    url(r'^editprofile/$',editprofile),
    url(r'^about/$',aboutpage),
    url(r'^linkWechat/$',linkWechat),
    url(r'^aboutTour/$',aboutTour),
    url(r'^member/$',member),
    url(r'^contact/$',contact),
]
