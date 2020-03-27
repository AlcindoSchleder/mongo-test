# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class MoviesCategory(models.Model):
    dsc_category = models.CharField(max_length=100, verbose_name='Category')
    sum_likes = models.IntegerField(default=0, verbose_name='Total Likes')
    sum_dislikes = models.IntegerField(default=0, verbose_name='Total Dislikes')
    ranking = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Ranking')

    class Meta:
        db_table = 'movies_category'
        verbose_name = 'Movies Category'
        verbose_name_plural = 'Movies Category'

    def __str__(self):
        return self.dsc_category


class Movies(models.Model):
    fk_movies_category = models.ForeignKey(
        MoviesCategory, on_delete=models.CASCADE, verbose_name='Category'
    )
    dsc_movie = models.TextField(verbose_name='Movie Description')
    qtd_likes = models.IntegerField(default=0, verbose_name='Likes')
    qtd_dislikes = models.IntegerField(default=0, verbose_name='Dislikes')
    ranking = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Ranking')

    class Meta:
        db_table = 'movies'
        verbose_name = 'Movies'
        verbose_name_plural = 'Movies'


class MoviesVotes(models.Model):
    fk_movies_category = models.ForeignKey(
        MoviesCategory, on_delete=models.CASCADE, verbose_name='Category'
    )
    fk_movies = models.ForeignKey(
        Movies, on_delete=models.CASCADE, verbose_name='Movie'
    )
    # a positive value to like and a negative value to dislike
    vote_movie = models.IntegerField(default=0, verbose_name='Vote')
    date_vote = models.DateTimeField(auto_now=True,  verbose_name='Date')

    class Meta:
        db_table = 'movies_votes'
        verbose_name = 'Movies Votes'
        verbose_name_plural = 'Movies Votes'


@receiver(post_save, sender=MoviesVotes)
def movies_post_save(instance, created, **kwargs):
    if not created:
        raise Exception('PostSave: Error on save data, table Movie Votes can not be edited!')
    try:
        category = MoviesCategory.objects.get(instance.fk_movies_category.id)
        movie = Movies.objects.get(instance.fk_movies.id)
    except ObjectDoesNotExist:
        raise Exception(f'PostSave: Error on get categories or movies! {ObjectDoesNotExist}')
    vote = instance.vote_movie if instance.vote_movie > 0 else instance.vote_movie * -1
    if instance.vote_movie > 0:
        category.sum_likes += vote
        movie.qtd_likes += vote
    else:
        category.sum_dislikes += vote
        movie.qtd_dislikes += vote
    movie.ranking = movie.qtd_likes - (movie.qtd_dislikes / 2)
    category.ranking = category.sum_likes - (category.sum_dislikes / 2)
    try:
        movie.save()
        category.save()
    except Exception as e:
        raise Exception(f'PostSave: Error on cla ranking! - ({e})')
