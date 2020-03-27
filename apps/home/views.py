# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .forms import MoviesForm, MoviesCategoryForm
from .models import MoviesCategory, Movies, MoviesVotes
from django.views.decorators.csrf import csrf_exempt


class HomeView(ListView):
    template_name = 'home/index.html'
    model = Movies
    paginate_by = 10

    def get_queryset(self):
        return Movies.objects.order_by('ranking')


class HomeMoviesView(TemplateView):
    form_class = MoviesForm
    template_name = 'home/movies.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})


class MoviesCategoryView(TemplateView):
    template_name = 'home/category.html'
    form_class = MoviesCategoryForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save()

            # Change the value of the "#id_author". This is the element id in the form

            return HttpResponse(
                f'<script>opener.closePopup(window, "{instance.pk}", "{instance}", "#id_author");</script>'
            )

        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            instance = form.save()

            # Change the value of the "#id_author". This is the element id in the form

            return HttpResponse(
                f'<script>opener.closePopup(window, "{instance.pk}", "{instance}", "#id_author");</script>')

        return render(request, self.template_name, {"form": form})

    @csrf_exempt
    def get_author_id(self, request, *args, **kwargs):
        if request.is_ajax():
            author_name = request.GET['author_name']
            author_id = MoviesCategory.objects.get(name=author_name).id
            data = {'author_id': author_id}
            return HttpResponse(json.dumps(data), content_type='application/json')
        return HttpResponse("/")
