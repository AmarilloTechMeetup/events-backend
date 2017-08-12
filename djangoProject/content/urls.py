from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^content$', views.list_content.as_view()),
    url(r'^category$', views.list_category.as_view()),
    url(r'^events$', views.list_event.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
