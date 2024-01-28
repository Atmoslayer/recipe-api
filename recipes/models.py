from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    name = models.CharField(
        'Название продукта',
        max_length=50,
    )

    number_of_uses = models.PositiveIntegerField(
        'Количество использований',
        default=0,
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        'Название рецепта',
        max_length=50,
    )

    description = models.TextField(
        'Описание',
        max_length=500,
        blank=True,
    )

    text = models.TextField(
        'Текст рецепта',
    )

    image = models.ImageField(
        'Картинка',
        upload_to='recipes_images',
    )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeProductItem(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        verbose_name='Рецепт',
        on_delete=models.CASCADE,
        related_name='recipe_items',
    )

    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        on_delete=models.CASCADE,
        related_name='product_items',
    )

    weight = models.PositiveIntegerField(
        'Вес продукта',
        validators=[MinValueValidator(1)],
    )

    class Meta:
        verbose_name = 'Продукт в рецепте'
        verbose_name_plural = 'Продукты в блюде'

    def __str__(self):
        return f'{self.product.name} для {self.recipe.name}'
