from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from callerapi.views import CallsViewSet
router = routers.DefaultRouter(trailing_slash=False)
router.register("calls", CallsViewSet, "call")
urlpatterns = [
    path('', include(router.urls)),
]

