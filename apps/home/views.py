# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.views.generic.edit import DeletionMixin
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .forms import MoviesForm, MoviesCategoryForm
from .models import MoviesCategory, Movies, MoviesVotes
from .mixin import UpdateMixin


class HomeView(ListView):
    template_name = 'home/index.html'
    model = Movies
    paginate_by = 8
    # context_object_name = 'movies'
    queryset = Movies.objects.order_by('fk_movies_category', 'ranking')


class HomeMoviesView(DeletionMixin, UpdateMixin, TemplateView):
    form_class = MoviesForm
    template_name = 'home/movies.html'
    success_url = 'home:index'
    http_method_names = ['get', 'post', 'delete', 'put', 'path']
    pk = None

    def initial_data(self):
        data = {
            'dsc_movie': '',
            'qtd_likes': 0,
            'qtd_dislikes': 0,
            'ranking': 0.00
        }
        if self.pk is not None:
            instance = Movies.objects.get(id=self.pk)
            data['fk_movies_category'] = instance.fk_movies_category
            data['dsc_movie'] = instance.dsc_movie
            data['qtd_likes'] = instance.qtd_likes
            data['qtd_dislikes'] = instance.qtd_dislikes
            data['ranking'] = instance.ranking
        return data

    def get(self, request, pk=None, *args, **kwargs):
        self.pk = pk
        init_data = self.initial_data()
        form = self.form_class(init_data)
        return render(request, self.template_name, {'form': form, 'category': ''})

    def post(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
        form = self.form_class(request.POST or None)
        if form.is_valid():
            if self.pk is None:
                instance = Movies()
            else:
                instance = Movies.objects.get(pk=self.pk)
            instance.fk_movies_category = form.cleaned_data['fk_movies_category']
            instance.dsc_movie = form.cleaned_data['dsc_movie']
            instance.qtd_likes = form.cleaned_data['qtd_likes']
            instance.qtd_dislikes = form.cleaned_data['qtd_dislikes']
            instance.ranking = form.cleaned_data['ranking']
            instance.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {"form": form})

    def delete(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            movie = Movies.objects.get(id=pk)
            movie.delete()
        return redirect(self.success_url)

    def put(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            movie = Movies.objects.get(pk=pk)
            category = MoviesCategory.objects.get(pk=movie.fk_movies_category_id)
            vote = MoviesVotes(
                fk_movies=movie, fk_movies_category=category, vote_movie=1
            )
            vote.save()
        return redirect(self.success_url)

    def path(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            movie = Movies.objects.get(pk=pk)
            category = MoviesCategory.objects.get(pk=movie.fk_movies_category_id)
            vote = MoviesVotes(
                fk_movies=movie, fk_movies_category=category, vote_movie=-1
            )
            vote.save()
        return redirect(self.success_url)


class MoviesCategoryView(TemplateView):
    template_name = 'home/category.html'
    form_class = MoviesCategoryForm
    pk = None

    def initial_data(self):
        data = {
            'dsc_category': '',
            'sum_likes': 0,
            'sum_dislikes': 0,
            'ranking': 0.00
        }
        if self.pk is not None:
            instance = MoviesCategory.objects.get(id=self.pk)
            data['dsc_category']: instance.dsc_category
            data['sum_likes']: instance.sum_likes
            data['sum_dislikes']: instance.sum_dislikes
            data['ranking']: instance.ranking
        return data

    def get(self, request, pk=None, *args, **kwargs):
        self.pk = pk
        form = self.form_class(self.initial_data())
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        self.pk = kwargs.get('pk')
        form = self.form_class(request.POST or None)
        if form.is_valid():
            if self.pk is None:
                instance = MoviesCategory()
            else:
                instance = MoviesCategory.objects.get(pk=self.pk)
            instance.dsc_category = form.cleaned_data['dsc_category']
            instance.sum_likes = form.cleaned_data['sum_likes']
            instance.sum_dislikes = form.cleaned_data['sum_dislikes']
            instance.ranking = form.cleaned_data['ranking']
            instance.save()
            return HttpResponse(
                '<script>closeWindow(window, ' +
                f'"{instance.pk}", "{instance}", "#fk_movies_category");</script>'
            )
        return render(request, self.template_name, {"form": form})

    @csrf_exempt
    def get_category_id(self, request, **kwargs):
        if request.is_ajax():
            dsc_category = request.GET['dsc_category']
            category_id = MoviesCategory.objects.get(name=dsc_category).id
            data = {'category_id': category_id}
            return HttpResponse(json.dumps(data), content_type='application/json')
        return HttpResponse("/")
