from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import Card
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from mtgsdk import Card
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

@login_required
def main_page(request):
    card = Card.where(name="Liliana of the Veil").all()
    print(card)
    return render(request, 'mtg/main_page.html', {'card': card})

@login_required
def deck_builder(request):
    cards = []
    i = 55
    response = [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]
    # cards.extend(Card.where(page=2).where(pageSize=100).all())
    while i < 57:
    # len(response) == 100:
        response = Card.where(page=i).where(pageSize=100).all()
        for card in response:
            string = card.flavor
            print(string.replace("sacrifice", "TAYLOR"))
            # print(string.replace("'", "TAYLOR"))
        cards.extend(response)
        i = i + 1
    return render(request, 'mtg/deck_builder.html', {'card': cards})