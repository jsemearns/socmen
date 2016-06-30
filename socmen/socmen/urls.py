from django.conf.urls import include, url
from django.contrib import admin

from base import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'socmen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^results/$', views.ResultsPageView.as_view(), name='home')
]
