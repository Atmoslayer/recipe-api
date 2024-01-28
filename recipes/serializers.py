from rest_framework import serializers

from .models import Dish, Ingredient, DishIngredientItem


class DishItemUpdateSerializer(serializers.ModelSerializer):
    ingredient_id = serializers.ModelField(model_field=Ingredient()._meta.get_field('id'))
    ingredient_quantity = serializers.ModelField(model_field=DishIngredientItem()._meta.get_field('quantity'))

    def update(self, instance, validated_data):
        ingredient = Ingredient.objects.get(id=validated_data['ingredient_id'])
        item, created = DishIngredientItem.objects.update_or_create(
            ingredient=ingredient,
            dish=instance,
            defaults={
                'quantity': validated_data['ingredient_quantity'],
            }
        )

        return item

    class Meta:
        model = Dish
        fields = ['ingredient_id', 'ingredient_quantity']

