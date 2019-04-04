from django.urls import include, path
from rest_auth import urls as restauth_urls

urlpatterns = [
    path('rest-auth/', include(restauth_urls)),
]
