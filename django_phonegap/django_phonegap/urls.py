from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from .api import LoginResource
from blog.views import home
from blog.api import PostingResource
v1_api = Api(api_name="v1")
v1_api.register(LoginResource())
v1_api.register(PostingResource())



urlpatterns = patterns('',
    url(r'^api/',include(v1_api.urls)),
    url(r'^$', home, name="home"),
    url(r'^admin/', include(admin.site.urls)),
)
