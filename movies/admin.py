# from django.contrib import admin
# from .models import Movie, Person
#
#
# # admin.site.register(Person)
# # admin.site.register(PersonManager)
# # admin.site.register(MovieImage)
# # admin.site.register(MovieManager)
# # admin.site.register(Movie)
# # admin.site.register(Role)
# # admin.site.register(VoteManager)
# # admin.site.register(Vote)
#
#
# class MovieAdmin(admin.ModelAdmin):
#     inlines = []
#     list_display = ("title", "year", "rating")
#     list_filter = ("rating", "year")
#     fields = (("title", "year"),("runtime","rating"),"plot",)
#     search_fields = ["title"]
#
#
# class ActorAdmin(admin.ModelAdmin):
#     list_display = ("first_name","last_name",)
#     search_fields = ("first_name","last_name",)
#
#     def name(self, obj):
#         return "{} {}".format(obj.first_name, obj.last_name)
#
#
# admin.site.register(Movie, MovieAdmin)
# admin.site.register(Person, ActorAdmin)
#
#
#
#
#
#


# class DirectorInline(admin.StackedInline):
#     model = Movie
#     fk_name = "director"
#     verbose_name = "director"
#     verbose_name_plural = "directors"
#     extra = 1
#
#
# class RoleInline(admin.StackedInline):
#     # model = Role
#     extra = 1
#     autocomplete_fields = ("person", "movie")
#
# class MovieAdmin(admin.ModelAdmin):
#     inlines = [
#         RoleInline,
#     ]
#     list_display = ("title", "year", "rating")
#     list_filter = ("rating")
#     fields = (
#         (
#             "title",
#             "year",
#         ),
#         ("runtime", "rating"),
#         "plot",
#         "director",
#         "writers",
#         "website",
#     )
#     autocomplete_fields = ("writers", "director")
#     search_fields = ("title")


# class WriterInline(admin.StackedInline):
#     model = Movie

# Register your models here.





















from django.contrib import admin
from .models import Movie, Actor  #MovieImage


# class MovieImagesInLine(admin.StackedInline):
#     model = MovieImage
#     extra = 1


class MovieAdmin(admin.ModelAdmin):
    inlines = [
        # MovieImagesInLine
    ]
    list_display = ("title", "year", "rating")
    list_filter = ("rating", "year")
    fields = (
        ("title", "year"),
        "runtime",
        "rating",
        "plot",
    )
    search_fields = ["title"]


class ActorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
    )
    search_fields = (
        "first_name",
        "last_name",
    )

    def name(self, obj):
        return "{} {}".format(obj.first_name, obj.last_name)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)