from django.shortcuts import render, get_object_or_404
from .models import Movie, Category

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'movies/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    movies = Movie.objects.filter(category=category)
    return render(request, 'movies/category_detail.html', {'category': category, 'movies': movies})
