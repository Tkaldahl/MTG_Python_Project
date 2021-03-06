from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Card
from .models import Card
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from mtgsdk import Card as SDKCard
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def main_page(request):
    return render(request, 'mtg/main_page.html')

def login_redirect(request):
    return render(request, 'mtg/main_page.html')

@login_required
def deck_builder(request):
    cards = Card.objects.all()
    card_names = []
    for card in cards:
        card_names.append(card.name)
    return render(request, 'mtg/deck_builder.html', {'card_names': card_names})


# The functions below are for development testing only
@login_required
def data_practice_page(request):
    cards = Card.objects.all()
    legalities_check = SDKCard.where(page=50).where(pageSize=100).all()
    return render(request, 'mtg/data_practice_page.html', {'legalities_check': legalities_check})

@login_required
def mtg_database_scraper(request):
    cards = []
    i = 1
    response = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
    # MTG API only allows 100 results at a time. The loop below pages through the database, and cleans up the data so we can print it to a webpage to copy into the database
    while len(response) == 100:
        response = SDKCard.where(page=i).where(pageSize=100).all()
        for card in response:
            card.name = card.name.replace("'", "\\'")
            if card.flavor != None:
                card.flavor = card.flavor.replace("'", "\\'")
            if card.text != None:
                card.text = card.text.replace("'", "\\'")
            if card.rulings != None:
                card.rulings = str(card.rulings)
                card.rulings = card.rulings.replace("\\", "")
                card.rulings = card.rulings.replace("'", "\\'")
            if card.colors != None:
                card.colors = ' '.join(card.colors)
            if card.color_identity != None:
                card.color_identity = ' '.join(card.color_identity)
            if card.subtypes != None:
                card.subtypes = ' '.join(card.subtypes)
            if card.supertypes != None:
                card.supertypes = ' '.join(card.supertypes)
            if card.printings != None:
                card.printings = ' '.join(card.printings)
            if card.legalities != None:
                card.legalities = str(card.legalities)
            if card.artist != None:
                card.artist = card.artist.replace("'", "\\'")
            if card.set_name != None:
                card.set_name = card.set_name.replace("'", "\\'")
        cards.extend(response)
        i = i + 1
        print(i)
    return render(request, 'mtg/mtg_database_scraper.html', {'cards': cards})