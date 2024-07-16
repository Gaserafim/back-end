from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from games.models import GameScore
from setup.utils import calculate_score_field


@receiver(post_save, sender=GameScore)
@receiver(post_delete, sender=GameScore)
def update_game_rating(sender, instance, **kwargs):
    game = instance.game

    if game:
        average_score = calculate_score_field(GameScore, 'game', game.id)
        game.rating = average_score if average_score is not None else 0.0
        game.save()
