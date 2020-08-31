from api import views as api_views
from django.urls import path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'customers', api_views.ProfileViewSet)

urlpatterns = [] + router.urls
