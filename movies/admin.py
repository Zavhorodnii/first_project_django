from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", )


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "draft", )
    list_filter = ("category", "year", )
    search_fields = ("title", "category__name", )
    inlines = [ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft", )
    # fields = (("actors", "directors", "genres", ), )
    fieldsets = (
        (None, {
            "fields": (("title", "tegline"),)
        }),
        (None, {
            "fields": ("description", "poster", )
        }),
        (None, {
            "fields": (("year", "world_premier", "country", ), )
        }),
        ("Actors", {
            "classes": ("collapse", ),
            "fields": (("actors", "directors", "genres", "category", ), )
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fess_in_world", ), )
        }),
        ("Options", {
            "fields": (("url", "draft", ), )
        }),
    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "email", "movies", )
    readonly_fields = ("name", "email", )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name", "url", )


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "age", )


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("ip", "star", )


@admin.register(MovieShots)
class MovieShots(admin.ModelAdmin):
    list_display = ("title", "movie", )


admin.site.register(RatingStar)