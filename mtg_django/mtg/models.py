from django.db import models

class Card(models.Model):
    name = models.CharField(max_length=100)
    multiverse_id = models.IntegerField(null=True)
    layout = models.CharField(max_length=100)
    mana_cost = models.CharField(max_length=100)
    cmc = models.IntegerField(null=True)
    colors = models.CharField(max_length=100)
    color_identity = models.CharField(max_length=100)
    card_type = models.CharField(max_length=100)
    supertypes = models.CharField(max_length=100)
    subtypes = models.CharField(max_length=100)
    rarity = models.CharField(max_length=100)
    text = models.TextField()
    flavor = models.TextField()
    artist = models.CharField(max_length=100)
    card_number = models.IntegerField(null=True)
    power = models.IntegerField(null=True)
    toughness = models.IntegerField(null=True)
    loyalty = models.IntegerField(null=True)
    rulings = models.TextField()
    printings = models.CharField(max_length=100)
    legalities = models.CharField(max_length=100)
    image_url = models.URLField(max_length=1000)
    card_set = models.CharField(max_length=100)
    set_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name