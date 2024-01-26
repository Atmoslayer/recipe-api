from django.core.validators import MinValueValidator
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(
        'Название ингредиента',
        max_length=50,
    )

    number_of_uses = models.PositiveIntegerField(
        'Количество использований',
        default=0,
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(
        'Название блюда',
        max_length=50,
    )

    description = models.TextField(
        'Описание',
        max_length=500,
        blank=True,
    )

    recipe = models.TextField(
        'Рецепт',
    )

    image = models.ImageField(
        'Картинка',
        upload_to='dishes_images',
    )

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.name


class DishIngredientItem(models.Model):
    dish = models.ForeignKey(
        Dish,
        verbose_name='Блюдо',
        on_delete=models.CASCADE,
        related_name='dish_items',
    )

    ingredient = models.ForeignKey(
        Ingredient,
        verbose_name='Ингредиент',
        on_delete=models.CASCADE,
        related_name='ingredient_items',
    )

    quantity = models.PositiveIntegerField(
        'Количество ингредиента',
        validators=[MinValueValidator(1)],
    )

    class Meta:
        verbose_name = 'Ингредиент в блюде'
        verbose_name_plural = 'Ингредиенты в блюде'

    def __str__(self):
        return f'{self.ingredient.name} для {self.dish.name}'
