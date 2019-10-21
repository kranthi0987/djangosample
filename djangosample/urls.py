"""djangosample URL Configuration

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
import patterns as patterns
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

from account import views
from djangosample import settings

schema_view = get_swagger_view(title="wallpaper API")
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('calc.urls')),
    path('api/', include('api.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('api.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^special/', views.special, name='special'),
    url(r'^account/', include('account.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('account/', include('useraccountapi.urls')),
    path('wallpapers/', include('wallpaperapi.urls')),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Wallpaper API')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
