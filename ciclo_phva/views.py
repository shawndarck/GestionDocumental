from django.shortcuts import render
from django.views import generic
from ciclo_phva.models import ItemEstandar

# Create your views here.
class ListarItemsEstandares(generic.ListView):
    item = ItemEstandar
