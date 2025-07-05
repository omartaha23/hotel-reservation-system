from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, UserViewSet, ReservationViewSet, ComplaintViewSet, ResponseViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reservations', ReservationViewSet)
router.register(r'complaints', ComplaintViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = router.urls
