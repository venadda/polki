"""polki_dolki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from vendor.views import UserViewSet,CustomerSerializer

from rest_framework_swagger.views import get_swagger_view
from vendor.views import *
schema_view = get_swagger_view(title='Polki-Dolki API')

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customer',CustomerViewSet)

urlpatterns = [
    path('router', include(router.urls)),
    path('admin/', admin.site.urls),
    path('vendor/',include('vendor.urls')),
    path('s/',schema_view),
    path('swagger/', include('swagger_ui.urls')),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('', include('siteapp.urls')),
]
