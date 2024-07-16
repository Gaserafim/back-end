from django.contrib import admin
from series.models import Series, SerieScore


class SeriesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "creator",
    )

    readonly_fields = ["rating",]

admin.site.register(Series, SeriesAdmin)


class SerieScoreAdmin(admin.ModelAdmin):
    list_display = ("serie",)

admin.site.register(SerieScore, SerieScoreAdmin)
