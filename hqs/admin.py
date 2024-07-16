from django.contrib import admin
from hqs.models import HQ, HQScore


class HQsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )

    readonly_fields = ["rating",]

admin.site.register(HQ, HQsAdmin)


class HQScoreAdmin(admin.ModelAdmin):
    list_display = ("hq",)

admin.site.register(HQScore, HQScoreAdmin)
