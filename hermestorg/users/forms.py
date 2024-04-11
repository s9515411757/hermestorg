from django.contrib.auth.forms import UserCreationForm
from .models import User


class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'flag_legal_entity', 'ogrn', 'document')

