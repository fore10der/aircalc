from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('loader/', include('loader.urls')),
    path('reporter/',include('reporter.urls')),
    path('error/',views.AccessDeniedTemplate.as_view(),name='error'),
    path('', include('base.urls'))
]