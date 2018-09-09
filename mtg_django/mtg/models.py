from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=500)
    multiverse_id = models.CharField(max_length=100)
    layout = models.CharField(max_length=100)
    mana_cost = models.CharField(max_length=100)
    cmc = models.CharField(max_length=100)
    colors = models.CharField(max_length=100)
    color_identity = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100)
    supertypes = models.TextField()
    subtypes = models.TextField()
    rarity = models.CharField(max_length=100)
    text = models.TextField()
    flavor = models.TextField()
    artist = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    toughness = models.CharField(max_length=100)
    loyalty = models.CharField(max_length=100)
    rulings = models.TextField()
    printings = models.TextField()
    legalities = models.TextField()
    image_url = models.URLField(max_length=1000)
    card_set = models.CharField(max_length=100)
    set_name = models.TextField()

    def __str__(self):
        return self.name


class Deck(models.Model):
    name = models.CharField(max_length=500)
    competitive_format = models.CharField(max_length=500)
    description = models.TextField(null=True)
    author = models.ForeignKey('auth.User', related_name='decks', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mainboard(models.Model):
    card_id = models.ForeignKey(Card, related_name='mainboard', null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    deck_id = models.ForeignKey(Deck, related_name='mainboard', on_delete=models.CASCADE)


class SideBoard(models.Model):
    card_id = models.ForeignKey(Card, related_name='sideboard', null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    deck_id = models.ForeignKey(Deck, related_name='sideboard', on_delete=models.CASCADE)
