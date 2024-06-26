from django.db import models
from django.contrib.auth import get_user_model
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

User = get_user_model()


class Сurrency(models.Model):
    name_currency = models.CharField(
        max_length=200,
        verbose_name="Название валюты",
        help_text="Укажите название валюты"
    )
    char_currency = models.CharField(
        max_length=10,
        verbose_name="Символ валюты",
        help_text="Укажите значок валюты символом"
    )
    currency_image = models.ImageField(
        verbose_name='Картинка валюты',
        help_text="Указжите картинку валюты",
        upload_to='currency_image/',
        blank=True,
        null=True
    )
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    def __str__(self):
        return self.name_currency

    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"


class Ip(models.Model):
    ip = models.CharField(max_length=15)
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "IP адресс"
        verbose_name_plural = "IP адреса"


class Card(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заглавие",
        help_text="Укажите название продукта"
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Название",
        help_text="Укажите название латиницей"
    )
    description = models.TextField(
        verbose_name="Название",
        help_text="Укажите описание группы"
    )
    category = TreeForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='Категория'
    )
    price = models.DecimalField(
        verbose_name='Стоимость',
        help_text = "Укажите стоимость продукта",
        max_digits=30,
        decimal_places=0,
        blank=True,
        null=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name='Автор',
        help_text="Автор поста"
    )
    number_of_views = models.ManyToManyField(
        Ip,
        related_name="card_views",
        blank=True,
        verbose_name="Просмотр",
        help_text="IP адрес, который просмотрел карточку товара"
    )
    address = models.CharField(
        max_length=200,
        verbose_name="Адрес",
        help_text="Укажите адрес, где находиться продукт"
    )
    currency = models.ForeignKey(
        Сurrency,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='currency',
        verbose_name='Валюта',
        help_text="Валюта продукта"
    )
    published = models.BooleanField(
        default=False,
        verbose_name='Флаг публикации',
        help_text="Опубликован продукт или нет"
    )
    moderation = models.BooleanField(
        default=False,
        verbose_name='Флаг публикации(модерации)',
        help_text="Публикуем ли объявление или нет"
    )
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )
    meta = models.CharField(
        max_length=1024,
        verbose_name="Мета",
        help_text="Мета JSON"
    )

    def get_absolute_url(self):
        return reverse('products:products', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(MPTTModel):
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название'
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        verbose_name='Родительская категория'
    )
    slug = models.SlugField(
        verbose_name="Название категории",
        help_text="Укажите название латиницей"
    )
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    class MPTTMeta:
        order_insertion_by = ['title']

    def get_absolute_url(self):
        return reverse(
            'post-by-category',
            args=[str(self.slug)]
        )

    def __str__(self):
        return self.title

    class Meta:
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение", default=0)
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField(
        verbose_name="IP адрес",
        max_length=15
    )
    star = models.ForeignKey(
        RatingStar,
        on_delete=models.PROTECT,
        verbose_name="Звезда рейтинга",
        help_text="Звезда рейтинга"
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.PROTECT,
        verbose_name="Продукт",
        help_text="Продукт"
    )
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    def __str__(self):
        return f"{self.star} - {self.card}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Comment(models.Model):
    card = models.ForeignKey(
        Card,
        related_name='comments',
        verbose_name='Комментарий продукта',
        help_text='Комментарий продукта',
        on_delete=models.PROTECT,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='comments',
        verbose_name='Автор комментария',
        help_text='Автор комментария',
    )
    text = models.TextField(
        max_length=1024,
        verbose_name='Текст комментария',
        help_text='Текст комментария',
    )
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    def __str__(self):
        return self.text[:self.CONSTANT_STR]

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик',
        help_text='Подписчик',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор подписки',
        help_text='Автор подписки',
    )
    flag = models.BooleanField(
        default=False,
        verbose_name='Активен',
        help_text="Активна подписка или нет"
    )
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    def __str__(self):
        return f"{self.user} подписан на -> {self.author}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'author'),
                name='user_and_author_unique'
            ),
            models.CheckConstraint(
                check=~models.Q(author=models.F('user')),
                name='author_and_user_are_not_the_same'
            )
        ]
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"


class Favourites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='favouriter',
        verbose_name='Пользователь',
        help_text='Выбирите пользователя',
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.SET_NULL,
        null=True,
        related_name='favouriting',
        verbose_name='Продукт',
        help_text='Добавьте продукт',
    )
    flag = models.BooleanField(
        default=False,
        verbose_name='Активен',
        help_text="Активна избранное или нет"
    )
    pub_date = models.DateTimeField(
        verbose_name='Создано',
        auto_now_add=True
    )
    pub_date_now = models.DateTimeField(
        verbose_name='Обновлено',
        auto_now=True
    )

    def __str__(self):
        return f"{self.user} добавил в избранное {self.card}"

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"