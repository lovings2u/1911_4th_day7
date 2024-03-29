"""naverapi URL Configuration

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
from django.contrib import admin
from django.urls import path

from search_trend import views as search_trend_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # 검색어를 입력하는 곳
    path('search/', search_trend_view.search),
    # 검색어에 대한 트랜드 결과를 받는 곳
    path('search/result', search_trend_view.result)

]
