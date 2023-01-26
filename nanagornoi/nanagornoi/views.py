from django.http import HttpResponse
from django.shortcuts import render


def steering_racks_page(request):
    return HttpResponse('Страница ремонта рулевых реек')


def turning_services_page(request):
    return HttpResponse('Страница токарных услуг')


def other_page(request):
    return HttpResponse('Страница прочих услуг')


def location_page(request):
    return HttpResponse('Страница месторасположения')


def contacts_page(request):
    return HttpResponse('Страница контактов')


def about_page(request):
    return HttpResponse('Страница "О нас"')
