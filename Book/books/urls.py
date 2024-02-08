from django.contrib import admin
from django.urls import path
from .views import CategoryViewSet,BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("category",CategoryViewSet,basename="category")
router.register("book",BookViewSet,basename="books")

urlpatterns = [
]+router.urls


