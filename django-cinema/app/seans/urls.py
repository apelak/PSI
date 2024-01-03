from rest_framework import routers
from django.urls import path, include
from .views import ShowingViewSet,Halls_SeatsViewSet, TicketViewSet, Cinema_HallViewSet

router = routers.DefaultRouter()
router.register(r'cinema_hall', Cinema_HallViewSet)
router.register(r'ticket', TicketViewSet)
router.register(r'showing', ShowingViewSet)
router.register(r'halls_seats', Halls_SeatsViewSet)
urlpatterns = [
    path('', include(router.urls))
]