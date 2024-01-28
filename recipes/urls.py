from rest_framework import routers

from .views import AddProductViewSet

router = routers.DefaultRouter()
router.register(r'add_product_to_recipe', AddProductViewSet, basename='items')

urlpatterns = router.urls
