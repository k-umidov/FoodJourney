from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=60,verbose_name='Название кухни')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

class Dish(models.Model):
    cuisine = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Название кухни')
    name_of_the_dish = models.CharField(max_length=60,verbose_name='Название блюда')
    description = models.TextField(verbose_name='Описание')
    history = models.TextField(verbose_name='История блюда')
    ingredients = models.TextField(verbose_name="Ингредиенты")
    cooking_time = models.PositiveIntegerField( verbose_name="Время приготовления (в минутах)")
    calories = models.PositiveIntegerField( verbose_name="Калорийность (ккал)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    photo = models.ImageField(upload_to='images/',verbose_name='Фотографие блюда')
    trailer = models.TextField(null=True,blank=True,verbose_name='Ссылка на ютуб видео приготовление')
    views = models.IntegerField(default=0,verbose_name='Просмотры')
    def __str__(self):
        return self.name_of_the_dish
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
class Comment(models.Model):
    text = models.CharField(max_length=300,verbose_name='Текст комментарии')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Автор')
    food = models.ForeignKey(Dish,on_delete=models.CASCADE,verbose_name='Еда')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата добавления')

    def __str__(self):
        return f'Комментарии от {self.author.username} для блюда {self.food.name_of_the_dish}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class ProfileUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Пользователь')
    photo = models.ImageField(upload_to='profile/',verbose_name='Фото профиля',null=True,blank=True)
    is_online = models.BooleanField(default=False,verbose_name='Статус профиля')
    about = models.CharField(max_length=250,verbose_name='О себе',null=True,blank=True)
    location = models.CharField(max_length=50,verbose_name='Место нахождения',null=True,blank=True)

    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return 'https://admgor.nnov.ru/uploads/editor/30/71/dfc4e28b59dfe79524d94646f9254c2c8e39def1.jpg'
    def count_comment(self):
        if self.user.comment_set.all():
            return self.user.comment_set.all().count()
        else:
            return 0

    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
    class Meta:
        verbose_name = 'Профиль '
        verbose_name_plural = 'Профили'

