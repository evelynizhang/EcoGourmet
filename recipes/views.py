from django.shortcuts import render, get_object_or_404, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm
from django.contrib.auth.decorators import login_required


@login_required
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    context = {
       "form": form,
    }
    return render(request, "recipes/create.html", context)


def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    # print(recipe.ingredients)
    context = {
        "recipe_object": recipe,
    }
    return render(request, "recipes/detail.html", context) #html auto in templates


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list": recipes,
    }
    return render(request, "recipes/list.html", context)


@login_required
def edit_recipe(request, id):
    post = get_object_or_404(Recipe, id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("show_recipe", id=id)
    else:
        form = RecipeForm(instance=post)

    context = {
        "post_object": post,
        "post_form": form,
    }
    return render(request, "recipes/edit.html", context)



def redirect_to_recipe_list(request):
    return redirect("recipe_list")



@login_required
def my_recipe_list(request):
    recipes=Recipe.objects.filter(author=request.user)
    context = {
        "recipe_list": recipes
    }
    return render(request, "recipes/list.html", context)
