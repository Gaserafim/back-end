from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from books.models import BookScore
from setup.utils import calculate_score_field


@receiver(post_save, sender=BookScore)
@receiver(post_delete, sender=BookScore)
def update_book_rating(sender, instance, **kwargs):
    book = instance.book

    if book:
        average_score = calculate_score_field(BookScore, 'book', book.id)
        book.rating = average_score if average_score is not None else 0.0
        book.save()
