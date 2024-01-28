from rest_framework import serializers
from rest_framework.response import Response

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


class RecipeProductIncreaseSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        recipe_products = Product.objects.filter(product_items__recipe=instance)
        for product in recipe_products:
            product.number_of_uses += 1
            product.save()
        return Response(
            {
                'dish': {
                    'id': instance.id,
                    'name': instance.name,
                },
                'products': [
                    {
                        'id': product.id,
                        'name': product.name,
                        'number_of_uses': product.number_of_uses
                    } for product in recipe_products
                ]
            }
        )

    class Meta:
        Fields = ()

