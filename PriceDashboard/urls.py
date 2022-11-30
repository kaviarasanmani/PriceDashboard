"""PriceDashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.homxe, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import poorvika_price,home_appliance,poorvika_price_filter
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('user.urls')),
    path('poorvika_filter',poorvika_price_filter.as_view(),name="filter"),
    path('poorvika',poorvika_price.as_view(),name="list"),

    path('home_appliance',home_appliance.as_view(),name="hK")


]
