from django.shortcuts import render


# Create your views here.
def steering_racks_page(request):
    return render(request, 'steering_racks.html')
