from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie, Category, Actor
from .forms import ReviewForm


class MovieView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movies.html"
    # def get(self, request):
    #     movies = Movie.objects.all()
    #     return render(request, "movies/movies.html", {"movie_list": movies})

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context["categories"] = Category.objects.all()
    #     return context


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"
    # def get(self, request, slug):
    #     movie = Movie.objects.get(url=slug)
    #     return render(request, "movies/movie_detail.html", {"movie": movie})


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        print('pk = {}'.format(pk))
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movies = movie
            form.save()
        print(request.POST)
        return redirect(movie.get_absolute_url())


class ActorView(DetailView):
    """Вывод информации об актере"""
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = "name"