import logging
from collections import Counter

import mpld3
import pytz
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.sites import requests
from django.db.models import Count, Sum
from django.db.models.functions import ExtractMonth
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
import requests
from matplotlib import pyplot as plt

from .forms import RegisterUserForm, LoginUserForm, FeedbackForm, CustomerForm, SellerForm, MebelForm, AddItemForm, \
    AddSpeciesForm, SearchForm, FilterForm
from .models import News, Feedbacks, About, FAQ, Contacts, Promocodes, Vacancies, Customer, Mebel, OrderItem, Order, \
    Seller
from django.views.generic import DetailView, CreateView

logging.basicConfig(level=logging.INFO, filename='logs.log', filemode='a',
                    format='%(asctime)s, %(levelname)s, %(message)s')


class viewnew(DetailView):
    model = News
    template_name = 'furnfactshop/onenew.html'
    context_object_name = 'onenew'  # передаем объект по названию context object name-a - onenew


def faq(request):
    faq = FAQ.objects.all()
    return render(request, 'furnfactshop/faq.html', {'faq': faq})


def contacts(request):
    try:
        contacts = Contacts.objects.all()
        logging.info('Successfully retrieved contacts')
    except:
        logging.info('Error')
    return render(request, 'furnfactshop/contacts.html', {'contacts': contacts})


def promocodes(request):
    promocodes = Promocodes.objects.all()
    logging.info('Successfully promocodes')
    return render(request, 'furnfactshop/promocodes.html', {'promocodes': promocodes})


def confidencial(request):
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    data = response.json()
    cat_fact = data["fact"]

    apiurl="https://api.ipify.org?format=json"
    response2=requests.get(apiurl)
    inf=response2.json()
    logging.info('Successfully confidencial')
    return render(request, 'furnfactshop/confidencial.html', {'fact': cat_fact,'inf':inf})

def vacancy(request):
    vacancy = Vacancies.objects.all()
    logging.info('Successfully vacancy')
    return render(request, 'furnfactshop/vacancy.html', {'vacancy': vacancy})


def method(request):
    user_tz=request.session.get('user_tz','UTC')
    current_time= timezone.now().astimezone(pytz.timezone(user_tz))
    news = News.objects.order_by('-date')[:1]
    logging.info('Successfully home')
    return render(request, 'furnfactshop/index.html', {'news': news, 'user_tz':user_tz, 'current_time':current_time})


def newurl(request):
    info = get_object_or_404(About)
    return render(request, 'furnfactshop/about.html', {'info': info})

def mebels(request):
    mebels=Mebel.objects.all
    logging.info('Successfully mebels')
    return render(request, 'furnfactshop/mebels.html', {'mebels':mebels})

def newshome(request):
    news = News.objects.order_by('-date')
    return render(request, 'furnfactshop/news.html', {'news': news})



def ratings(request):
    feedbacks = Feedbacks.objects.all
    return render(request, 'furnfactshop/feedbacks.html', {'feedbacks': feedbacks})


class BaseViewContextMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['title'] = kwargs.get('title', 'Default Title')
        return context


class RegisterView(BaseViewContextMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'furnfactshop/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(BaseViewContextMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'furnfactshop/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))


class LogoutUser(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')


@login_required
def add_feedback(request):
    error = ''
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.name = request.user.username
            feedback.save()
            return redirect('feedbacks')
        else:
            error = 'Неверное заполнение'
    form = FeedbackForm()
    data = {'error': error, 'form': form}
    return render(request, 'furnfactshop/add_feedback.html', data)

def customer(request):
    error = ''
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            cust = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            cust.user = user
            cust.save()
            return redirect('home')
        else:
            error = 'Неверное заполнение'
    form = CustomerForm()
    data = {'error': error, 'form': form}
    return render(request, 'furnfactshop/customer.html', data)

def seller(request):
    error = ''
    if request.method == "POST":
        form = SellerForm(request.POST)
        if form.is_valid():
            sell = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            sell.user = user
            sell.save()
            return redirect('home')
        else:
            error = 'Вам должно быть 18 лет'
    form = SellerForm()
    data = {'error': error, 'form': form}
    return render(request, 'furnfactshop/seller.html', data)

@login_required
def add_mebel(request):
    try:
        seller=Seller.objects.get(user=request.user)
    except Seller.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        form = MebelForm(request.POST)
        if form.is_valid():
            mebel=form.save(commit=False)
            mebel.company=seller
            mebel.save()
            return redirect('home')
    else:
        form = MebelForm()
    return render(request, 'furnfactshop/add_mebel.html', {'form': form})

@login_required
def add_to_cart(request, mebel_id):
    try:
        customer = Customer.objects.get(user=request.user)
    except Customer.DoesNotExist:
        return redirect('home')
    mebel = Mebel.objects.get(pk=mebel_id)
    if mebel.isSelling==False:
        return redirect('mebels')
    if request.method == 'POST':
        count = int(request.POST.get('count'))
        order_item, created = OrderItem.objects.update_or_create(object=mebel, user=request.user, defaults={'count': count})
        order, _ = Order.objects.update_or_create(user=request.user)
        order.mebels.add(order_item)
        return redirect('mebels')
    return render(request, 'furnfactshop/add_to_order.html')


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)

    if request.method == 'POST':
        order_item_id = request.POST.get('order_item_id')
        order_item = OrderItem.objects.get(pk=order_item_id)
        order_item.delete()
        return redirect('order_list')

    total_cost = 0
    ord = OrderItem.objects.filter(user=request.user)
    for order in ord:
        total_cost += order.count * order.object.price
    promocodes = Promocodes.objects.filter(work=True)
    totalpromo = total_cost
    for promocode in promocodes:
        totalpromo -= promocode.about
    totalpromo = max(totalpromo, 0)
    return render(request, 'furnfactshop/order_list.html', {'orders': orders, 'total_cost': total_cost, 'totalpromo': totalpromo})

@login_required
def add_species(request):
    try:
        seller=Seller.objects.get(user=request.user)
    except Seller.DoesNotExist:
        return redirect('home')
    if request.method == 'POST':
        form = AddSpeciesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddSpeciesForm()
    return render(request, 'furnfactshop/add_species.html', {'form': form})


def generate_plot():
    order_items = OrderItem.objects.all()
    mebel_counts = Counter()

    for item in order_items:
        mebel_counts[item.object.name] += item.count

    mebels = list(mebel_counts.keys())
    counts = list(mebel_counts.values())

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(counts, labels=mebels, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(mebels))))
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title('Частота заказов товаров')

    html_graph = mpld3.fig_to_html(fig)
    plt.close(fig)

    return html_graph

def foradmin(request):
    html_graph = generate_plot()
    customers_by_city = Customer.objects.order_by('city')
    aggregated_items = OrderItem.objects.values('object__name').annotate(total_count=Sum('count')).order_by('-total_count')
    mebel_with_highest_demand=aggregated_items.first()

    return render(request, 'furnfactshop/foradmin.html', {'mebel_with_highest_demand': mebel_with_highest_demand,'customers_by_city':customers_by_city, 'aggregated_items':aggregated_items,'graph': html_graph})


@login_required
def order_list_company(request):
    user_seller = Seller.objects.get(user=request.user)
    orders_with_company_products = OrderItem.objects.filter(object__company=user_seller).order_by('-user')
    orders = orders_with_company_products
    return render(request, 'furnfactshop/sellerurl.html', {'orders': orders})

def filter_mebels(request):
    form = FilterForm()
    results = []

    if 'company' in request.GET:
        form = FilterForm(request.GET)
        if form.is_valid():
            selected_company = form.cleaned_data['company']
            if selected_company:
                results = Mebel.objects.filter(company=selected_company)

    return render(request, 'furnfactshop/filter.html', {'form': form, 'results': results})

def search_view(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Mebel.objects.filter(name__icontains=query)

    return render(request, 'furnfactshop/search.html', {'form': form, 'query': query, 'results': results})


@login_required
def edit_mebel(request, mebel_id):
    mebel = get_object_or_404(Mebel, id=mebel_id)
    if request.method == 'POST':
        form = MebelForm(request.POST, instance=mebel)
        if form.is_valid():
            form.save()
            return redirect('companymebel')
    else:
        form = MebelForm(instance=mebel)
    return render(request, 'furnfactshop/edit_mebel.html', {'form': form})

@login_required
def delete_mebel(request, mebel_id):
    mebel = get_object_or_404(Mebel, id=mebel_id)
    if request.method == 'POST':
        mebel.delete()
        return redirect('companymebel')
    return render(request, 'furnfactshop/delete_mebel.html', {'mebel': mebel})

@login_required
def company_mebels(request):
    user_seller = Seller.objects.get(user=request.user)
    mebels = Mebel.objects.filter(company=user_seller)
    return render(request, 'furnfactshop/company_items.html', {'mebels':mebels})


@login_required
def update_order_item(request, item_id):
    order_item = get_object_or_404(OrderItem, id=item_id)
    if request.method == 'POST':
        new_count = int(request.POST.get('count', order_item.count))
        if new_count > 0:
            order_item.count = new_count
            order_item.save()
        return redirect('order_list')  # обновите это на ваше представление со списком заказов
    return redirect('order_list')  # обновите это на ваше представление со списком заказов

@login_required
def delete_order_item(request, item_id):
    order_item = get_object_or_404(OrderItem, id=item_id)
    if request.method == 'POST':
        order_item.delete()
    return redirect('order_list')  # обновите это на ваше представление со списком заказов