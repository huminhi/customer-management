from rest_framework.routers import DefaultRouter

from src.api.customers.views import CustomerView

router = DefaultRouter(trailing_slash=False)
router.register(r'', CustomerView)

urlpatterns = router.urls
