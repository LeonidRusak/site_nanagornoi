from django.shortcuts import render


# Create your views here.
def contacts_page(request):
    # Функция представления для страницы контактов
    return render(request, 'contacts.html')
