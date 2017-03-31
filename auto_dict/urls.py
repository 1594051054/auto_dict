from django.conf.urls import include,url
from . import views
app_name = "auto_dict"

urlpatterns = [
    url(r'^word_search/(?P<word>\w+)/$', views.word_search, name = 'word_search'),
]
