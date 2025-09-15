from rest_framework.routers import DefaultRouter
from django.urls import path, include
from polls.api.views import PollsViewSet

router = DefaultRouter()
router.register(r"polls", PollsViewSet, basename="polls")

urlpatterns = [
    path("", include(router.urls)),
]