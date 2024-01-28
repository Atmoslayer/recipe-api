from rest_framework import serializers

from .models import Recipe, Product, RecipeProductItem


class RecipeItemUpdateSerializer(serializers.ModelSerializer):
    product_id = serializers.ModelField(model_field=Product()._meta.get_field('id'))
    weight = serializers.ModelField(model_field=RecipeProductItem()._meta.get_field('weight'))

    def update(self, instance, validated_data):
        product = Product.objects.get(id=validated_data['product_id'])
        item, created = RecipeProductItem.objects.update_or_create(
            product=product,
            recipe=instance,
            defaults={
                'weight': validated_data['weight'],
            }
        )

        return item

    class Meta:
        model = Recipe
        fields = ['product_id', 'weight']

