# -*- coding: utf-8 -*-
from django import forms
from .models import Movies, MoviesCategory


class MoviesForm(forms.ModelForm):
    fk_movies_category = forms.ModelChoiceField(
        queryset=MoviesCategory.objects.all(), label='Category', help_text='Category'
    )
    dsc_movie = forms.CharField(
        label='Movie Description', help_text='Movie Description'
    )
    qtd_likes = forms.IntegerField(label='Likes', help_text='Likes')
    qtd_dislikes = forms.IntegerField(label='Dislikes', help_text='Dislikes')
    ranking = forms.DecimalField(
        max_digits=11, decimal_places=2, label='Ranking', help_text='Ranking'
    )

    class Meta:
        model = Movies
        fields = ('fk_movies_category', 'dsc_movie')
        read_only = ('qtd_likes', 'qtd_dislikes', 'ranking')


class MoviesCategoryForm(forms.Form):

    class Meta:
        model = MoviesCategory
        fields = ('dsc_category',)
        read_only = ('qtd_likes', 'qtd_dislikes', 'ranking')
