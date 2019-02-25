from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .settings import base as settings
from .utils import anonymous_required
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/',include('api.urls')),
    path('', anonymous_required(auth_views.LoginView.as_view()), name='login'),
    path('logout/', auth_views.LogoutView.as_view(),{'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('upload/', include('loader.urls')),
    path('report/',include('reporter.urls')),
    path('error/',views.AccessDeniedTemplate.as_view(),name='error'),
    path('redirect/', views.redirect, name='redirect')
]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = views.redirect
