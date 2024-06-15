from django.contrib import admin
from .models import News, About, Feedbacks, FAQ, Contacts, Promocodes, Vacancies, MebelSpecies, Mebel, Order, Customer, \
    Seller, OrderItem, Points
from .stats import orders_count


admin.site.register(News)
admin.site.register(Feedbacks)
admin.site.register(About)
admin.site.register(FAQ)
admin.site.register(Contacts)
admin.site.register(Vacancies)
admin.site.register(Promocodes)
admin.site.register(Mebel)
admin.site.register(MebelSpecies)
admin.site.register(Order)
admin.site.register(Seller)
admin.site.register(Customer)
admin.site.register(OrderItem)
admin.site.register(Points)