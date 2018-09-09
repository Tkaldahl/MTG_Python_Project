from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('deck_builder', views.deck_builder, name='deck_builder'),
    path('data_practice_page', views.data_practice_page, name='data_practice_page'),
    path('mtg_database_scraper', views.mtg_database_scraper, name='mtg_database_scraper'),
]