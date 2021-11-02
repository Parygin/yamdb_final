from django.contrib import admin

from .models import Category, Comment, CustomUser, Genre, Review, Title


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'text', 'author', 'score', 'pub_date'
    )
    search_fields = ('author',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'text', 'author', 'pub_date')
    search_fields = ('author',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'description', 'year', 'category'
    )
    search_fields = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'role', 'bio')
    search_fields = ('role',)


admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(CustomUser, UserAdmin)
