from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'home.html', {'greeting': 'HTMl файл основного тела страницы'})
