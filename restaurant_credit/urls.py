"""
URL configuration for restaurant_credit project.

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CustomerViewSet, MealViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # JWT endpoints

router = DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='customer') # Registering the customer viewset with the router
router.register(r'meals', MealViewSet, basename='meal') # Meal viewset router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # JWT auth tokens
    path('api/auth-token', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/auth-token-refresh', TokenRefreshView.as_view(), name='token-refresh')
]
