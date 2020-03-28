# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .forms import MoviesForm, MoviesCategoryForm
from .models import MoviesCategory, Movies, MoviesVotes
from django.views.decorators.csrf import csrf_exempt


class HomeView(ListView):
    template_name = 'home/index.html'
    model = Movies
    paginate_by = 8
    # context_object_name = 'movies'
    queryset = Movies.objects.order_by('fk_movies_category', 'ranking')


class HomeMoviesView(TemplateView):
    form_class = MoviesForm
    template_name = 'home/movies.html'

    @staticmethod
    def initial_data(pk = None):
        if pk is None:
            return {
                'dsc_movie': '',
                'qtd_likes': 0,
                'qtd_dislikes': 0,
                'ranking': 0.00
            }
        return MoviesCategory.objects.get(id=pk)

    def get(self, request, *args, **kwargs):
        form = self.form_class(self.initial_data())
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = Movies()
            instance.fk_movies_category = form.cleaned_data['fk_movies_category']
            instance.dsc_movie = form.cleaned_data['dsc_movie']
            instance.qtd_likes = form.cleaned_data['qtd_likes']
            instance.qtd_dislikes = form.cleaned_data['qtd_dislikes']
            instance.ranking = form.cleaned_data['ranking']
            instance.save()
            return redirect('home:index')
        return render(request, self.template_name, {"form": form})


class MoviesCategoryView(TemplateView):
    template_name = 'home/category.html'
    form_class = MoviesCategoryForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(self.initial_data())
        # if form.is_valid():
        #     instance = form.save()
        #     # Change the value of the "#id_author". This is the element id in the form
        #     return HttpResponse(
        #         '<script>MoviesEvents.closeWindow(window, ' +
        #         f'"{instance.pk}", "{instance}", "#fk_movies_category");</script>'
        #     )
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = MoviesCategory()
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

    @staticmethod
    def initial_data(pk=None):
        if pk is None:
            return {
                'dsc_category': '',
                'sum_likes': 0,
                'sum_dislikes': 0,
                'ranking': 0.00
            }
        return MoviesCategory.objects.get(id=pk)

    def edit_category(self, request, pk):
        if request is not None and len(request.POST) > 0:
            form = self.form_class(request.POST)
            if form.is_valid():
                instance = form.save()
                # Change the value of the "#fk_movies_category". This is the element id in the form
                return HttpResponse(
                    '<script>MoviesEvents.closeWindow(window, ' +
                    f'"{instance.pk}", "{instance}", "#fk_movies_category");</script>')
        else:
            form = self.form_class(self.initial_data(pk))
            return render(request, self.template_name, {"form": form})

    @csrf_exempt
    def get_category_id(self, request, **kwargs):
        if request.is_ajax():
            dsc_category = request.GET['dsc_category']
            category_id = MoviesCategory.objects.get(name=dsc_category).id
            data = {'category_id': category_id}
            return HttpResponse(json.dumps(data), content_type='application/json')
        return HttpResponse("/")
