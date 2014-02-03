from django.conf.urls import patterns, include, url
from django.contrib import admin
#from books.views import search_form,search,register,user_login1,index1,restricted,user_logout,latest,latest1,rate,popular 
from books.views import *
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pycode.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search_form/$',search_form),
    url(r'^search/$',search),
    url(r'^register/$',register),
    url(r'^login/$',user_login1),
    url(r'^index/$',index1),
    url(r'^latest/$',latest),                   
    url(r'^latest1/$',latest1),
    url(r'^rate/$',rate),
    url(r'^popular/$',popular),                   
)
