"""ChatServerPlayground URL Configuration

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
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from personal.views import (
	home_screen_view
)

urlpatterns = [
	path('', home_screen_view, name='home'),
	path('admin/', admin.site.urls),
    # path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('dashboard/', include('dashboard.urls')),
    path('security/', include('security.urls')),
    path('customer/', include('customer.urls')),
    path('accounts/', include('allauth.urls')),
    path('device/', include('device.urls')),
    
    #path('friend/', include('friend.urls', namespace='friend')),
    #path('login/', login_view, name="login"),
    #path('logout/', logout_view, name="logout"),
    #path('register/', register_view, name="register"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


