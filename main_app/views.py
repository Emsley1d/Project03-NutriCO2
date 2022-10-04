from unicodedata import name
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe, Ingredient, User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.contrib import messages

# Create your views here.


#RECIPES CRUD
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = '__all__'

    # def recipe_form(self, request):
    #     if request.method == "POST":
    #         form = recipe_form(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, 'Recipe added succesfully.')
    #             return render(request, 'recipes/index.html', { 'recipes': recipe})

    #         else:
    #             messages.error(request, 'Invalid form; please try again')
    #             return render(request, 'home.html')
            
                             

class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = '__all__'

class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = '/recipes/'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def recipes_index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', { 'recipes': recipes})

@login_required
def recipes_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes/detail.html'),


#INGREDIENTS CRUD

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient

class IngredientDetail(LoginRequiredMixin, DetailView):
    model = Ingredient

class IngredientCreate(LoginRequiredMixin, CreateView):
    model = Ingredient
    fields = '__all__'

class IngredientUpdate(LoginRequiredMixin, UpdateView):
    model = Ingredient
    fields = '__all__'

class IngredientDelete(LoginRequiredMixin, DeleteView):
    model = Ingredient
    success_url = '/ingredients/'


def ingredients_index(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredients/index.html', { 'ingredients': ingredients})

def ingredients_detail(request, ingredient_id):
    ingredient = Ingredient.objects.get(id=ingredient_id)
    return render(request, 'ingredients/detail.html', { 'ingredients': ingredient})

def signup(request):
    error_message =""
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your registration was successful')
            return redirect('/')
    
            
        else:
            messages.error(request, 'Your registration was unsuccessful; please try again later')
            return redirect('/')  



    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

#ASSOCIATE AND UNASSOCIATE INGREDIENTS WITH RECIPES

def assoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id = recipe_id).ingredients.add(ingredient_id)
    return redirect('detail', recipe_id = recipe_id)

def unassoc_ingredient(request, recipe_id, ingredient_id):
    Recipe.objects.get(id = recipe_id).ingredients.remove(ingredient_id)
    return redirect('detail', recipe_id = recipe_id)

#NAV BAR
def nav_view(request):
    return render(request, "nav.html")

#USER DETAILS
def user_detail(request, user_id):
    user = User.objects.get(id=user_id)
    return render(request, 'user/detail.html', { 'user': user})



#USER CRUD
class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    fields = '__all__'

class UserCreate(LoginRequiredMixin, CreateView):
    model = User
    fields = '__all__'

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = '__all__'

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = '/'







