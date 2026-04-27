"""
URL configuration for storefront project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    # 🛠️ Admin
    path('admin/', admin.site.urls),

    # 🔐 AUTH CORE
    path('api/', include('core.urls')),

    # 🔑 JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # 📦 APPS
    path('api/store/', include('store.urls')),
 #   path('api/likes/', include('likes.urls')),
  #  path('api/tags/', include('tags.urls')),

    # 🧪 PLAYGROUND (tests)
    path('playground/', include('playground.urls')),
    
    # API schema (backend JSON)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI (interface web)
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    # Redoc (alternative propre)
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]