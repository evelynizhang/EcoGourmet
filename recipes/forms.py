from django.forms import ModelForm
from recipes.models import Recipe


class RecipeForm(ModelForm):
    class Meta: #inner class to customize the form we want
        model = Recipe
        fields = (
            "title",
            "picture",
            "description",
        )


