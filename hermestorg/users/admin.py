from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'email', 'flag_legal_entity', 'ogrn', 'document')
    search_fields = ('first_name', 'last_name', 'username', 'email', 'flag_legal_entity', 'ogrn',)
    list_filter = ('pub_date',)


admin.site.register(User, UserAdmin)