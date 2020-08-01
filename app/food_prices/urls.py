from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"chicken", views.ChickenViewSet)

urlpatterns = router.urls
