from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = {
    url(r'^content$', views.list_content.as_view()),
    url(r'^category$', views.list_category.as_view()),
    url(r'^content/', views.content_by_param.as_view()),
}

urlpatterns = format_suffix_patterns(urlpatterns)
