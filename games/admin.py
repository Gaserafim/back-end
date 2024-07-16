from django.contrib import admin
from games.models import Game, GameScore


class GamesAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "developer",
    )

    readonly_fields = ["rating",]

admin.site.register(Game, GamesAdmin)


class GameScoreAdmin(admin.ModelAdmin):
    list_display = ("game",)

admin.site.register(GameScore, GameScoreAdmin)
