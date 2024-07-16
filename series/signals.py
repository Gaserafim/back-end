from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from series.models import SerieScore
from setup.utils import calculate_score_field


@receiver(post_save, sender=SerieScore)
@receiver(post_delete, sender=SerieScore)
def update_serie_rating(sender, instance, **kwargs):
    serie = instance.serie

    if serie:
        average_score = calculate_score_field(SerieScore, 'serie', serie.id)
        serie.rating = average_score if average_score is not None else 0.0
        serie.save()
