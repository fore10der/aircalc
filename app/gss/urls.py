from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from . import views
from .settings import base as settings
from .utils import anonymous_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', anonymous_required(auth_views.LoginView.as_view()), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('upload/', include('loader.urls')),
    path('report/',include('reporter.urls')),
    path('error/',views.AccessDeniedTemplate.as_view(),name='error'),
    re_path(r'^.*', views.redirect, name='redirect')
]

