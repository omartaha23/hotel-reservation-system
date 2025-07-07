from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'complaint', ComplaintViewSet)


urlpatterns = [
    path('', include(router.urls))
]