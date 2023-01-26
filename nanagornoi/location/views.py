from django.shortcuts import render


# Create your views here.
def location_page(request):
    return render(request, 'location.html')
