from django.urls import include, path
from django.conf.urls import url

from rest_framework import urls as restframework_urls

from rest_auth import urls as restauth_urls
from rest_auth.registration import urls as restauth_registration_urls

urlpatterns = [
    path('api-auth/', include(restframework_urls)),
    path('', include(restauth_urls)),
    path('registration', include(restauth_registration_urls)),
]
