from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),  # список фильмов
    path('<int:pk>/', views.movie_detail, name='movie_detail'),  # детальный просмотр фильма
    path('categories/', views.category_list, name='category_list'),  # список категорий
    path('categories/<int:pk>/', views.category_detail, name='category_detail'),  # категория
]

