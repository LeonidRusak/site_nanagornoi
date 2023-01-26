from django.shortcuts import render


# Create your views here.
def other_page(request):
    return render(request, 'other.html')
