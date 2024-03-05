from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipes_view(request, recipe):
    servings = int(request.GET.get('servings', 1))
    data_recipe = DATA.get(recipe)
    data_values = {ing: amount * servings for ing, amount in data_recipe.items()}
    context = {
        "servings": servings,
        "recipe":
            data_values
    }
    return render(request, 'calculator/dish.html', context)

def dishes_view(request):
    dishes_names = DATA.keys()
    context = {
        "dishes_names": dishes_names
    }
    print(dishes_names)
    return render(request, 'calculator/index.html', context)
