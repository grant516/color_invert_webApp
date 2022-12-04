"""my_site URL Configuration

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
from django.urls import path
from weather import views as wv
from color_mathcher import views as cv

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("my_weather/", wv.my_weather, name = "my_weather"),
    # path("nws_weather/<str:site>", wv.nws_weather, name = "nws_weather"),
    path("color/", cv.adding_color, name = "color")
]
