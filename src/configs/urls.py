"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.admindocs import urls as admindocs_urls

from health_check import urls as healthcheck_urls
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from apis import urls as apis_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/docs/', include(admindocs_urls)),
    # Health checks:
    path('health/', include(healthcheck_urls)),
    path('docs/', include_docs_urls(title='DRF APIs')),
    path('schema/', get_schema_view(title='DRF APIs')),
    path('api/v1/', include(apis_urls)),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        # URLs specific only to django-debug-toolbar:
        url('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
