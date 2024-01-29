from rest_framework import routers

from .views import UpdateRecipeProductViewSet, IncreaseRecipeProductViewSet

router = routers.DefaultRouter()
router.register('add_product_to_recipe', UpdateRecipeProductViewSet, basename='add_products')
router.register('cook_recipe', IncreaseRecipeProductViewSet, basename='increase_products')

urlpatterns = router.urls
