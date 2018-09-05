from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('deck_builder', views.deck_builder, name='deck_builder')
]