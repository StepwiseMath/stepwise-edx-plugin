from rest_framework.routers import DefaultRouter
from stepwise_plugin.api.views import ConfigurationViewSet

router = DefaultRouter(trailing_slash=False)
router.register("configuration", ConfigurationViewSet)
urlpatterns = router.urls
