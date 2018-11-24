"""TechieNest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from blog import urls as blog_urls
from company import urls as company_urls
from download import urls as download_urls
from events import urls as events_urls
from franchise import urls as franchise_urls
from jap import urls as jap_urls
from services import urls as services_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^blog/',include(blog_urls)),
    re_path(r'^company/',include(company_urls)),
    re_path(r'^download/',include(download_urls)),
    re_path(r'^events/',include(events_urls)),
    re_path(r'^franchise/',include(franchise_urls)),
    re_path(r'^jap/',include(jap_urls)),
    re_path(r'^services/',include(services_urls)),
]
