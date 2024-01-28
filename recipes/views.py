from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import Dish
from .serializers import DishItemUpdateSerializer


class AddProductViewSet(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishItemUpdateSerializer
