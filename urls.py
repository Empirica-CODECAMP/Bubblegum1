"""
URL configuration for bubblegum1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from file_manager.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', home_page, name='home')
    path('', include('file_manager.urls')),    
    path('health-index/', include('health_index.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    
    
admin.site.site_header = 'BUBBLEGUM'
admin.site.site_title = 'BUBBLEGUM'
admin.site.index_title = 'BUBBLEGUM admin'  