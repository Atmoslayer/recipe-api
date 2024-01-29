from django.db.models import Prefetch, Q
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Recipe, RecipeProductItem
from .serializers import RecipeItemUpdateSerializer, RecipeProductIncreaseSerializer


class UpdateRecipeProductViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeItemUpdateSerializer


class IncreaseRecipeProductViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeProductIncreaseSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.instance.data)


def show_recipes_without_product(request, product_id):

    forbidden_items = RecipeProductItem.objects.filter(Q(product_id=product_id, weight__gte=10))
    available_recipes = Recipe.objects.exclude(recipe_items__in=forbidden_items)

    context = {
        'recipes': [
            {
                'id': recipe.id,
                'name': recipe.name,
            } for recipe in available_recipes
        ]
    }

    return render(request, template_name='main.html', context=context)