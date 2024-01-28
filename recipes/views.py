from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Recipe
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
