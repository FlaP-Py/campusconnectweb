"""campusconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^signin', 'app.views.signin'),
    url(r'^start', 'app.views.start'),
    url(r'^home', 'app.views.home'),
    url(r'^course', 'app.views.course_page'),
    url(r'^notebook', 'app.views.notes_page'),
    url(r'^profile', 'app.views.profile'),
    url(r'^search_action', 'app.views.search_action'),
    url(r'^search', 'app.views.search_page'),
    url(r'^upload_page', 'app.views.upload_page'),
    url(r'^upload', 'app.views.upload'),
    url(r'^sign_up', 'app.views.sign_up')



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
