from django.db import models
from django.conf import settings




class Recipe(models.Model):
    title = models.CharField(max_length=100)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  #true:auto assign time to now(the time it got created), you don't need to do it manually

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True,
    )
    def __str__(self):
        return self.title


class RecipeStep(models.Model):
    step_number = models.PositiveBigIntegerField()
    instruction = models.TextField()
    recipe = models.ForeignKey(
        "Recipe",
        related_name="steps",
        on_delete=models.CASCADE
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ["step_number"]


class Ingredient(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        "Recipe",
        related_name="ingredients",
        on_delete=models.CASCADE
    )

    def recipe_title(self):
        return self.recipe.title

    class Meta:
        ordering = ["food_item"]
