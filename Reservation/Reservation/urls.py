from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, UserViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)


urlpatterns = [
    path('', include(router.urls))
]