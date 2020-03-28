# -*- coding: utf-8 -*-
from django.urls import path
from .views import HomeView, HomeMoviesView, MoviesCategoryView

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('movies/', HomeMoviesView.as_view(), name='movies'),
    path('category/', MoviesCategoryView.as_view(), name="category"),
    path('category/<int:pk>', MoviesCategoryView.as_view(), name="edit_category"),
    # path(
    #     'category/ajax/get_category_id',
    #     'MoviesCategoryView.get_category_id',
    #     name="category_ajax"
    # ),
]
