from django.urls import path
from . import views

app_name = 'culture'

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),

    # Articles
    path('articles/', views.articles_list, name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),

    # Destinations
    path('destinations/', views.destinations_list, name='destinations'),
    path('destinations/<slug:slug>/', views.destination_detail, name='destination_detail'),

    # Crafts
    path('crafts/', views.crafts_list, name='crafts'),
    path('crafts/<slug:slug>/', views.craft_detail, name='craft_detail'),
]