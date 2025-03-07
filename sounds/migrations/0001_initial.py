# Generated by Django 5.0.7 on 2024-07-16 15:43

import django.core.validators
import django.db.models.deletion
import setup.validations
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('release_date', models.IntegerField(validators=[setup.validations.validate_publication_date])),
                ('genre', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
            ],
        ),
        migrations.CreateModel(
            name='SoundScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('date_score', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(10)])),
                ('sound', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sounds.sound')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
