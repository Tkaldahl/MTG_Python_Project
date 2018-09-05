from django import forms
from .models import Card

class Card(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('name', 'multiverse_id','layout', 'mana_cost', 'cmc', 'colors', 'color_identity', 'card_type', 'supertypes', 'subtypes', 'rarity', 'text', 'flavor', 'artist', 'card_number', 'power', 'toughness', 'loyalty', 'rulings', 'printings', 'legalities', 'image_url', 'card_set', 'set_name')
