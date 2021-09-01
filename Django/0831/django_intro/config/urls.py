"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# 앞에 어떠한 패턴이 있던지 그게 오면 뒤에서는 거기에서만 처리하겠다. blog가 앞에 왔으니 blog.urls에서만 처리

from django.contrib import admin
from django.urls import path, include
from articles import views as art_views
from accounts import views as acc_views


urlpatterns = [
    # accounts app에서 하는 일
    # path('accounts/index/', acc_views.index),
    path('accounts/', include('accounts.urls')),

    # articles app에서 하는 일 
    path('articles/', include('articles.urls')),
    # path('<username>/<article_number>/', art_views.read),
    # path('catch/', art_views.catch),
    # path('throw/', art_views.throw),
    # path('dinner/', art_views.dinner),
    # path('greeting/', art_views.greeting),
    # path('articles/index/', art_views.index),
    path('admin/', admin.site.urls),
]
