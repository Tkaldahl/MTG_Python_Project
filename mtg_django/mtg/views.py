from django.shortcuts import render
from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

# Create your views here.
def main_page(request):
    card = Card.find(386616)
    return render(request, 'mtg/main_page.html', {'card': card})
