from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf import settings
from . import views


urlpatterns = [
    re_path(r'^add_to_cart/(?P<mebel_id>\d+)/$', views.add_to_cart, name='add_to_cart'),
    path('', views.method, name='home'),
    path('about/', views.newurl, name='about'),
    path('news/', views.newshome, name='news'),
    path('feedbacks/', views.ratings, name='feedbacks'),
    path('news/<int:pk>', views.viewnew.as_view(), name='onenew'), #pk - primary key - первичный ключ
    path('faq/', views.faq,     name='faq'),
    path('vacancy/', views.vacancy,     name='vacancy'),
    path('confidencial/', views.confidencial,     name='confidencial'),
    path('contacts/', views.contacts,     name='contacts'),
    path('promocodes/', views.promocodes,     name='promocodes'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('addfeedback/', views.add_feedback, name='addfeedback'),
    path('customer/', views.customer, name='customer'),
    path('seller/', views.seller, name='seller'),
    path('mebels/', views.mebels, name='mebels'),
    path('add_mebel/', views.add_mebel, name='add_mebel'),
    path('orders/', views.order_list, name='order_list'),
    path('order/item/update/<int:item_id>/', views.update_order_item, name='update_order_item'),
    path('order/item/delete/<int:item_id>/', views.delete_order_item, name='delete_order_item'),
    path('add_species/', views.add_species, name='add_species'),
    path('foradmin/', views.foradmin, name='foradmin'),
    path('orderlistcompany/', views.order_list_company, name='order_list_company'),
    path('search/', views.search_view, name='search'),
    path('filter/', views.filter_mebels, name='filter'),
    path('mebel/edit/<int:mebel_id>/', views.edit_mebel, name='edit_mebel'),
    path('mebel/delete/<int:mebel_id>/', views.delete_mebel, name='delete_mebel'),
    path('companymebel/', views.company_mebels, name='companymebel'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
