from django.db.models import Avg
from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS, IsAuthenticated, \
    IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Film, Review
from .serializers import FilmSerializer, ReviewSerializer


class IsAdminOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)


class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        review_id = self.request.data.get('film')
        serializer.save(user_added=self.request.user, film=review_id)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)


class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        review_id = self.request.data.get('film')
        serializer.save(user_added=self.request.user, film=review_id)



class TopFilmsListView(generics.ListAPIView):
    queryset = Film.objects.annotate(avg_rating=Avg('review__rating')).order_by('-avg_rating')[:10]
    serializer_class = FilmSerializer
