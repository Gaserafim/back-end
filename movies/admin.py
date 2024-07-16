from django.contrib import admin
from movies.models import Movie, MovieScore


class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "director",
    )

    readonly_fields = ["rating",]

admin.site.register(Movie, MoviesAdmin)


class MovieScoreAdmin(admin.ModelAdmin):
    list_display = ("movie",)

admin.site.register(MovieScore, MovieScoreAdmin)
