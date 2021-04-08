from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api_app import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('moment', views.UserMomentViewSet)

urlpatterns = [
        path('', include(router.urls)),
        path('login/', views.UserLoginApiView.as_view())
]
