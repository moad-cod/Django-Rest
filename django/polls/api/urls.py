from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PollsViewSet

polls_router = DefaultRouter()
polls_router.register(r"polls", PollsViewSet, basename="polls")