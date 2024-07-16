from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)
from setup.validations import validate_publication_date

User = get_user_model()


class HQ(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.IntegerField(validators=[validate_publication_date])
    genre = models.CharField(max_length=255)
    rating = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )

    def __str__(self):
        return self.title


class HQScore(models.Model):
    hq = models.ForeignKey(HQ, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(
        default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    date_score = models.DateTimeField(auto_now_add=True)
    description = models.TextField(validators=[MinLengthValidator(10)], max_length=1000)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
