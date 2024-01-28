from rest_framework import routers

from .views import UpdateRecipeProductViewSet, IncreaseRecipeProductViewSet

router = routers.DefaultRouter()
router.register(r'add_product_to_recipe', UpdateRecipeProductViewSet, basename='items')
router.register(r'cook_recipe', IncreaseRecipeProductViewSet, basename='increase_products')

urlpatterns = router.urls
