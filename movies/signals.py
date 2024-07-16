from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from movies.models import MovieScore
from setup.utils import calculate_score_field


@receiver(post_save, sender=MovieScore)
@receiver(post_delete, sender=MovieScore)
def update_movie_rating(sender, instance, **kwargs):
    movie = instance.movie

    if movie:
        average_score = calculate_score_field(MovieScore, 'movie', movie.id)
        movie.rating = average_score if average_score is not None else 0.0
        movie.save()
