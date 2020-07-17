
from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet

#API endpoints for the user model

router = routers.DefaultRouter()  # defines the standard REST endpoints
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]