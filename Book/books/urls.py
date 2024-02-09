from django.contrib import admin
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("category",CategoryViewSet,basename="category")
router.register("book",BookViewSet,basename="books")

urlpatterns = [
    path("borrow/",BorrowView.as_view(),name="borrow"),
    path("return/",ReturnView.as_view(),name="return")
]+router.urls


