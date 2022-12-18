from django.db import models

# Create your models here.

# Create your models here.
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


# Create your models here.
class Category(models.Model):
    """Категории"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Жанры"""
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Actor(models.Model):
    """Актеры и режиссеры"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="actors//")

    def __str__(self):
        return self.name


class Movie(models.Model):
    """Фильм"""
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    category = models.ManyToManyField(Category, related_name='film_category')
    genres = models.ManyToManyField(Genre, related_name='film_genre')
    poster = models.ImageField('Постер', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Дата выхода', default=2019)
    country = models.CharField('Страна', max_length=30)
    actors = models.ManyToManyField(Actor, related_name='film_actor')

    def __str__(self):
        return self.title


class Review(models.Model):
    """Комментарии """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.movie} - {self.owner}'


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')
    like = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.movie} - {self.owner} - {self.like}'


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ], blank=True, null=True
    )

    def __str__(self):
        return f'{self.movie} - {self.owner}  - {self.rating}'


class Image(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/')
