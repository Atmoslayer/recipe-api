from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Recipe
from .serializers import RecipeItemUpdateSerializer


class UpdateRecipeProductViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeItemUpdateSerializer


class