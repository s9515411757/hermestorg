from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('flag_legal_entity', 'ogrn', 'document')
    search_fields = ('ogrn',)
    list_filter = ('pub_date',)


admin.site.register(User, UserAdmin)