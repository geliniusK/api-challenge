"""jungle_news_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path
from rest_auth.views import PasswordResetConfirmView
from rest_framework.documentation import include_docs_urls
from django.contrib.auth import views as auth_views


API_TITLE = 'Jungle News API'
API_DESCRIPTION = 'Jungle Devs - Django Challenge #001'

urlpatterns = [
    path('api/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('admin/', admin.site.urls),
    path('api/', include('articles.urls')),
    path('api/', include('rest_auth.urls')),
    path('api/sign-up/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
