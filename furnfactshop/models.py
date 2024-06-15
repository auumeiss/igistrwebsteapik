import pytz
from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.db import models




class News(models.Model): #заголовок + кр содержание + картинка + вся статья
    title = models.CharField('Заголовок', max_length=50)
    anons = models.CharField('Краткое содержание', max_length=250)
    full_text = models.TextField('Вся статья', max_length=2500)
    image = models.ImageField('Картинка для публикации', upload_to='static')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
    date = models.DateTimeField('Дата публикации')

class Rating(models.IntegerChoices):
    ONE = 1, 'One'
    TWO = 2, 'Two'
    THREE = 3, 'Three'
    FOUR = 4, 'Four'
    FIVE = 5, 'Five'

class Feedbacks(models.Model): #отзывы
    name = models.CharField('Имя пользователя', max_length=20)
    rating = models.IntegerField()
    text = models.TextField('Отзыв', max_length=2500)

    def __str__(self):
        return f"{self.name} {self.rating}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    dating=models.DateField('Дата публикации', auto_now_add=True)

class About(models.Model):
    logo = models.ImageField('Логотип')
    aboutcompany = models.TextField('Рассказ о компании')
    requisites = models.TextField('Реквизиты')
    video = models.FileField('Видео о компании', upload_to='static')

    def __str__(self):
        return self.requisites
    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'

class FAQ(models.Model):
    question = models.CharField('Вопрос', max_length=100)
    answer = models.CharField('Ответ', max_length=500)
    date=models.DateField('Дата добавления')
    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Ответ на вопрос'
        verbose_name_plural = 'Ответы на вопросы'


class Contacts(models.Model):

    name = models.CharField('Имя', max_length=10)
    email = models.EmailField('Емаил сотрудника')
    aboutwork=models.TextField('Выполняемая работа', max_length=500)
    phone_number = models.CharField('Номер телефона',max_length=15,validators=[RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )],blank=True)
    image = models.ImageField('Фото', upload_to='static')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

class Vacancies(models.Model):

     name = models.CharField('Название вакансии', max_length=25)
     about = models.TextField('О вакансии', max_length=500)

     def __str__(self):
         return self.name

     class Meta:
         verbose_name = 'Вакансия'
         verbose_name_plural = 'Вакансии'

class Promocodes(models.Model):
    work = models.BooleanField('Действует или в нет (в архиве)?', default=True)
    name = models.CharField('Промокод', max_length=30)
    about = models.IntegerField('Сколько (в рублях)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name=models.CharField('Имя пользователя', max_length=20)
    phone_number = models.CharField('Номер телефона', max_length=15, validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )], blank=True)
    city=models.CharField('Город',max_length=20)
    adress=models.CharField('Адрес', max_length=100)
    email=models.EmailField('Почта')
    birth_date = models.DateField('Дата рождения', null=True, blank=True)


    def __str__(self):
        return self.name

class Points(models.Model):
    name=models.CharField('Название точки', max_length=50)
    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField('Имя пользователя', max_length=20)
    companyname = models.CharField('Название компании', max_length=20)
    points=models.ManyToManyField(Points, related_name='Tochki', blank=True)
    birth_date = models.DateField('Дата рождения',null=True, blank=True)
    def __str__(self):
        return self.companyname

class MebelSpecies(models.Model):
    species=models.CharField('Вид', max_length=10)
    def __str__(self):
        return self.species

class Mebel(models.Model):
    image = models.ImageField('Картинка для публикации', upload_to='static')
    company = models.ForeignKey(Seller, related_name='company', on_delete=models.CASCADE)
    name = models.CharField('Наименование', max_length=30)
    price = models.IntegerField('Цена', max_length=10)
    code = models.CharField('Код товара', max_length=10)
    species=models.ForeignKey(MebelSpecies, related_name='vid', on_delete=models.CASCADE)
    model=models.CharField('Модель', max_length=10)
    isSelling=models.BooleanField('Производится\снято с производства (галочка = производится')
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    count=models.IntegerField('Количество объекта')
    object=models.ForeignKey(Mebel, related_name='mebelnik', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


class Order(models.Model):
    user=models.OneToOneField(User, related_name='orders',on_delete=models.CASCADE)
    date=models.DateField('Дата заказа', auto_now_add=True)
    mebels=models.ManyToManyField(OrderItem, related_name='zakazi', blank=True)
    promo=models.OneToOneField(Promocodes, related_name='promo', blank=True, null=True, on_delete=models.CASCADE)
