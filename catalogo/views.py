from django.shortcuts import render, get_object_or_404
from .models import Pais, Itinerary

# Lista todos os países
def country_list(request):
    countries = Pais.objects.all().order_by('nome')
    context = {'countries': countries}
    return render(request, 'catalogo/country_list.html', context)

# Detalhe de um país e seus itinerários
def country_detail(request, country_id):
    country = get_object_or_404(Pais, id=country_id)
    itineraries = country.itineraries.all().order_by('data_inicio')  # relaciona itinerários ao país
    context = {
        'country': country,
        'itineraries': itineraries
    }
    return render(request, 'catalogo/country_detail.html', context)

# Lista todos os roteiros
def itinerary_list(request):
    itineraries = Itinerary.objects.all().order_by('data_inicio')
    context = {'itineraries': itineraries}
    return render(request, 'catalogo/itinerary_list.html', context)

# Detalhe de um roteiro específico
def itinerary_detail(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, id=itinerary_id)
    context = {'itinerary': itinerary}
    return render(request, 'catalogo/itinerary_detail.html', context)
