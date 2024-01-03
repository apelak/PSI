from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS, \
    IsAuthenticated

from .models import Cinema_Hall, Showing, Ticket,  Halls_Seats
from .serializers import Cinema_HallSerializer,Halls_SeatsSerializer, ShowingSerializer, TicketSerializer


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


class Cinema_HallViewSet(viewsets.ModelViewSet):
    serializer_class = Cinema_HallSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Cinema_Hall.objects.all()


class Halls_SeatsViewSet(viewsets.ModelViewSet):
    serializer_class = Halls_SeatsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Halls_Seats.objects.all()


class ShowingViewSet(viewsets.ModelViewSet):
    serializer_class = ShowingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Showing.objects.all()


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

