from rest_framework import routers
from django.urls import path, include
from .views import FilmViewSet, ReviewViewSet, ReviewCreateAPIView

router = routers.DefaultRouter()
router.register(r'films', FilmViewSet)
router.register(r'reviews', ReviewViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('reviews/create/', ReviewCreateAPIView.as_view(), name="review-create")
]