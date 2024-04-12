from django.contrib.auth import get_user_model
from django.db import models


PERSON = (
    ('P', 'Физическое лицо'),
    ('L', 'Юридическое лицо'),
)


class User(get_user_model()):
    flag_legal_entity = models.CharField(verbose_name='Лицо', max_length=1, choices=PERSON, default=PERSON[1][1])
    ogrn = models.DecimalField(verbose_name='ОГРН', max_digits=13, decimal_places=0, blank=True, null=True)
    document = models.ImageField(verbose_name='Документ', upload_to='documents/', blank=True, null=True)
    pub_date = models.DateTimeField(verbose_name='Дата авторизации', auto_now_add=True)

    def __str__(self):
        return self.first_name