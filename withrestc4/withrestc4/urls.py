"""withrestc4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from rest_framework import routers
from testapp import views
router= routers.DefaultRouter()
router.register('api',views.EmployeeCRUDCBV,base_name='api')
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include(router.urls)),
    #url(r'^get-api-token',views.obtain_auth_token,name='get_api_token'),
    url(r'^get-obtain-jwt/',obtain_jwt_token),
    url(r'^get-refresh-jwt/',refresh_jwt_token),
    url(r'^get-verify-jwt/',verify_jwt_token),

]
