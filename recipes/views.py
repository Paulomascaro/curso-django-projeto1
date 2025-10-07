
from django.shortcuts import render
# Create your views here.

# HTTP REQUEST
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Paulo R. Mascaro',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'name': 'Paulo R. Mascaro',
    })
