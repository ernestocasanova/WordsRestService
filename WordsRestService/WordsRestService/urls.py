from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers
from app.api import views

router = routers.DefaultRouter()
router.register(r'api/v1/words', views.WordsViewSet)

urlpatterns = [
    url(r'^', include(router.urls), name='main_app'),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]