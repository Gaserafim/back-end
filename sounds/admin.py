from django.contrib import admin
from sounds.models import Sound, SoundScore


class SoundsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "artist",
    )

    readonly_fields = ["rating",]

admin.site.register(Sound, SoundsAdmin)


class SoundScoreAdmin(admin.ModelAdmin):
    list_display = ("sound",)

admin.site.register(SoundScore, SoundScoreAdmin)
