from django.shortcuts import render


# Create your views here.
def turning_services_page(request):
    return render(request, 'turning_services.html')
