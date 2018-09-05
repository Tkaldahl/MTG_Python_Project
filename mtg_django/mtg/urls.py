from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('mtg_database_scraper', views.mtg_database_scraper, name='mtg_database_scraper')
]