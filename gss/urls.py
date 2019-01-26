from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loader/', include('loader.urls')),
    path('reporter/',include('reporter.urls')),
    path('', include('base.urls'))
]
