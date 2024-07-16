from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from hqs.models import HQScore
from setup.utils import calculate_score_field


@receiver(post_save, sender=HQScore)
@receiver(post_delete, sender=HQScore)
def update_hq_rating(sender, instance, **kwargs):
    hq = instance.hq

    if hq:
        average_score = calculate_score_field(HQScore, 'hq', hq.id)
        hq.rating = average_score if average_score is not None else 0.0
        hq.save()
