from datetime import date

from bootstrap_datepicker_plus.widgets import DatePickerInput
import pytz
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models import TextField
from django.forms import forms, CharField, PasswordInput, TextInput, Select, Textarea, Form, IntegerField, ModelForm, \
    ChoiceField, NumberInput, EmailField, HiddenInput, ModelChoiceField, DateField, SelectDateWidget, DateInput

from .models import Feedbacks, Rating, Customer, Seller, Mebel, Order, OrderItem, MebelSpecies


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-input'}))

class SellerForm(ModelForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
    name = CharField(label='Имя пользователя', max_length=20,
                     widget=TextInput(attrs={'class': 'form-input'}))
    companyname = CharField(label='Имя компании', max_length=20,
                     widget=TextInput(attrs={'class': 'form-input'}))
    birth_date = DateField(label='Дата рождения',
                                 widget=SelectDateWidget(years=range(1900, date.today().year + 1)))
    class Meta:
        model = Seller
        fields = ['username','password','name', 'companyname','birth_date']

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if age < 18:
            raise forms.ValidationError("Вам должно быть больше 18 лет.")
        return birth_date
class CustomerForm(ModelForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))
    name=CharField(label='Имя пользователя',max_length=20,
                   widget=TextInput(attrs={'class': 'form-input'}))
    phone_number=CharField(label='Номер телефона', max_length=15, validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )], widget=TextInput(attrs={'class': 'form-input'}))

    city = CharField(label='Город', max_length=20, widget=TextInput(attrs={'class': 'form-input'}))
    adress = CharField(label='Адрес', max_length=100, widget=TextInput(attrs={'class': 'form-input'}))
    email = EmailField(label='Почта', widget=TextInput(attrs={'class': 'form-input'}))
    birth_date = DateField(help_text='Date of birth', widget=DateInput(attrs={'type': 'date'}))


    class Meta:
        model = Customer
        fields = ['username','password','name', 'phone_number','city','adress','email', 'birth_date']

    def clean_birth_date(self):
        birth_date = self.cleaned_data['birth_date']
        if birth_date:
            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            if age < 18:
                raise forms.ValidationError("You must be at least 18 years old to register.")
        return birth_date

class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input'}))

class FeedbackForm(ModelForm):
    rating = ChoiceField(
        label='Рейтинг',
        choices=[(i, i) for i in range(1, 6)],
        widget=Select(attrs={'class': 'form-select'})
    )
    text = CharField(
        label='Отзыв',
        widget=Textarea(attrs={'class': 'form-input', 'rows': 4, 'cols': 200})
    )
    class Meta:
        model = Feedbacks
        fields = ['rating', 'text']


class MebelForm(ModelForm):
    class Meta:
        model = Mebel
        fields = ['name', 'price', 'code', 'species', 'model', 'isSelling', 'image']

class SearchForm(ModelForm):
    class Meta:
        model = Mebel
        fields = ['query']
    query = CharField(label='Поиск', max_length=100)
class AddItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['object', 'count']
        widgets = {
            'object': HiddenInput(),
        }

class AddSpeciesForm(ModelForm):
    class Meta:
        model=MebelSpecies
        fields=['species']

class FilterForm(forms.Form):
    company = ModelChoiceField(
        queryset=Seller.objects.all(),
        label='Компания',
        required=False
    )

