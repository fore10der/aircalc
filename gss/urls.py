from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('report/', include('app.urls')),    #new

    path('loader/', include('loader.urls')),
    path('', include('base.urls'))
]