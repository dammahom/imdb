from django.conf.urls import include, url

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'items', views.ItemViewSet, 'items')

urlpatterns = [
    url(r'^$', 'imdb.views.index'),
    url(r'^logged_in/$', 'imdb.views.logged_in'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'imdb/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'imdb/logout.html'}),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', views.UserViewSet.as_view()),
    url(r'^items/$', views.ItemViewSet.as_view()),
]
