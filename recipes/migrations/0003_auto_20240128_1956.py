# Generated by Django 3.2.15 on 2024-01-28 16:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_ingredient_number_of_uses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название продукта')),
                ('number_of_uses', models.PositiveIntegerField(default=0, verbose_name='Количество использований')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название рецепта')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Описание')),
                ('text', models.TextField(verbose_name='Текст рецепта')),
                ('image', models.ImageField(upload_to='recipes_images', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='RecipeProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Вес продукта')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_items', to='recipes.product', verbose_name='Продукт')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_items', to='recipes.recipe', verbose_name='Рецепт')),
            ],
            options={
                'verbose_name': 'Продукт в рецепте',
                'verbose_name_plural': 'Продукты в блюде',
            },
        ),
        migrations.RemoveField(
            model_name='dishingredientitem',
            name='dish',
        ),
        migrations.RemoveField(
            model_name='dishingredientitem',
            name='ingredient',
        ),
        migrations.DeleteModel(
            name='Dish',
        ),
        migrations.DeleteModel(
            name='DishIngredientItem',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
    ]