from django.contrib import admin
from django.urls import path
from .views import CategoryViewSet,BookViewSet,BorrowView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("category",CategoryViewSet,basename="category")
router.register("book",BookViewSet,basename="books")

urlpatterns = [
    path("borrow/",BorrowView.as_view(),name="borrow")
]+router.urls


