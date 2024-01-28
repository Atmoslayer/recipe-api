from rest_framework import routers

from .views import UpdateRecipeProductViewSet

router = routers.DefaultRouter()
router.register(r'add_product_to_recipe', UpdateRecipeProductViewSet, basename='items')

urlpatterns = router.urls
