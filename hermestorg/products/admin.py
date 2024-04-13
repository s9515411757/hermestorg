from django.contrib import admin
from .models import (
    Сurrency,
    Ip,
    Card,
    Category,
    RatingStar,
    Rating,
    Comment,
    Favourites,
    Follow
)


@admin.register(Сurrency)
class СurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'name_currency',
        'char_currency',
        'currency_image',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'name_currency',
        'char_currency',
        'currency_image',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)


@admin.register(Ip)
class IpAdmin(admin.ModelAdmin):
    list_display = (
        'ip',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'ip',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description',
        'category',
        'price',
        'author',
        'address',
        'currency',
        'published',
        'moderation',
        'meta',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'title',
        'slug',
        'description',
        'category',
        'price',
        'author',
        'address',
        'currency',
        'published',
        'moderation',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'parent',
        'slug',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'title',
        'parent',
        'slug',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = (
        'value',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'value',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = (
        'ip',
        'star',
        'card',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'ip',
        'star',
        'card',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'card',
        'author',
        'text',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'card',
        'author',
        'text',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'author',
        'flag',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'user',
        'author',
        'flag',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)


@admin.register(Favourites)
class FavouritesAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'card',
        'flag',
        'pub_date',
        'pub_date_now'
    )
    search_fields = (
        'user',
        'card',
        'flag',
        'pub_date',
        'pub_date_now'
    )
    list_filter = ('pub_date',)