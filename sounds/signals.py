from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from sounds.models import SoundScore
from setup.utils import calculate_score_field


@receiver(post_save, sender=SoundScore)
@receiver(post_delete, sender=SoundScore)
def update_sound_rating(sender, instance, **kwargs):
    sound = instance.sound

    if sound:
        average_score = calculate_score_field(SoundScore, 'sound', sound.id)
        sound.rating = average_score if average_score is not None else 0.0
        sound.save()
