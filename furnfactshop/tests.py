from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from .models import News, Feedbacks, About, FAQ, Contacts, Vacancies, Promocodes, Customer, Seller, MebelSpecies, Mebel, OrderItem, Order

# Create your tests here.
class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.news = News.objects.create(title='Test Title', anons='Test Anons', full_text='Test Full Text', image='test.jpg', date='2024-01-01')
        self.feedback = Feedbacks.objects.create(name='Test User', rating=5, text='Test Feedback')
        self.about = About.objects.create(logo='logo.jpg', aboutcompany='Test About Company', requisites='Test Requisites', video='video.mp4')
        self.faq = FAQ.objects.create(question='Test Question', answer='Test Answer', date='2024-01-01')
        self.contact = Contacts.objects.create(name='Test Contact', email='test@example.com', aboutwork='Test Work', phone_number='+123456789', image='contact.jpg')
        self.vacancy = Vacancies.objects.create(name='Test Vacancy', about='Test Vacancy About')
        self.promocode = Promocodes.objects.create(work=True, name='Test Promocode', about=100)
        self.seller = Seller.objects.create(user=self.user, name='Test Seller', companyname='Test Company')
        self.species = MebelSpecies.objects.create(species='Test Species')
        self.mebel = Mebel.objects.create(company=self.seller, name='Test Mebel', price=100, code='123456', species=self.species, model='Test Model', isSelling=True)
        self.order_item = OrderItem.objects.create(count=1, object=self.mebel, user=self.user)
        self.order = Order.objects.create(user=self.user)

    def test_news_creation(self):
        self.assertEqual(self.news.title, 'Test Title')
        self.assertEqual(self.news.anons, 'Test Anons')
        self.assertEqual(self.news.full_text, 'Test Full Text')
        self.assertEqual(self.news.image, 'test.jpg')
        self.assertEqual(self.news.date, '2024-01-01')

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.name, 'Test User')
        self.assertEqual(self.feedback.rating, 5)
        self.assertEqual(self.feedback.text, 'Test Feedback')

    def test_news_creation5(self):
        self.assertEqual(self.news.title, 'Test Title')
        self.assertEqual(self.news.anons, 'Test Anons')
        self.assertEqual(self.news.full_text, 'Test Full Text')
        self.assertEqual(self.news.image, 'test.jpg')
        self.assertEqual(self.news.date, '2024-01-01')

    def setUp1(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.news = News.objects.create(title='Test Title', anons='Test Anons', full_text='Test Full Text', image='test.jpg', date='2024-01-01')
        self.feedback = Feedbacks.objects.create(name='Test User', rating=5, text='Test Feedback')
        self.about = About.objects.create(logo='logo.jpg', aboutcompany='Test About Company', requisites='Test Requisites', video='video.mp4')
        self.faq = FAQ.objects.create(question='Test Question', answer='Test Answer', date='2024-01-01')
        self.contact = Contacts.objects.create(name='Test Contact', email='test@example.com', aboutwork='Test Work', phone_number='+123456789', image='contact.jpg')
        self.vacancy = Vacancies.objects.create(name='Test Vacancy', about='Test Vacancy About')
        self.promocode = Promocodes.objects.create(work=True, name='Test Promocode', about=100)
        self.seller = Seller.objects.create(user=self.user, name='Test Seller', companyname='Test Company')
        self.species = MebelSpecies.objects.create(species='Test Species')
        self.mebel = Mebel.objects.create(company=self.seller, name='Test Mebel', price=100, code='123456', species=self.species, model='Test Model', isSelling=True)
        self.order_item = OrderItem.objects.create(count=1, object=self.mebel, user=self.user)
        self.order = Order.objects.create(user=self.user)

    def test_feedback_creation1(self):
        self.assertEqual(self.feedback.name, 'Test User')
        self.assertEqual(self.feedback.rating, 5)
        self.assertEqual(self.feedback.text, 'Test Feedback')

    def test_news_creation(self):
        self.assertEqual(self.news.title, 'Test Title')
        self.assertEqual(self.news.anons, 'Test Anons')
        self.assertEqual(self.news.full_text, 'Test Full Text')
        self.assertEqual(self.news.image, 'test.jpg')
        self.assertEqual(self.news.date, '2024-01-01')

    def setUp1(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.news = News.objects.create(title='Test Title', anons='Test Anons', full_text='Test Full Text', image='test.jpg', date='2024-01-01')
        self.feedback = Feedbacks.objects.create(name='Test User', rating=5, text='Test Feedback')
        self.about = About.objects.create(logo='logo.jpg', aboutcompany='Test About Company', requisites='Test Requisites', video='video.mp4')
        self.faq = FAQ.objects.create(question='Test Question', answer='Test Answer', date='2024-01-01')
        self.contact = Contacts.objects.create(name='Test Contact', email='test@example.com', aboutwork='Test Work', phone_number='+123456789', image='contact.jpg')
        self.vacancy = Vacancies.objects.create(name='Test Vacancy', about='Test Vacancy About')
        self.promocode = Promocodes.objects.create(work=True, name='Test Promocode', about=100)
        self.seller = Seller.objects.create(user=self.user, name='Test Seller', companyname='Test Company')
        self.species = MebelSpecies.objects.create(species='Test Species')
        self.mebel = Mebel.objects.create(company=self.seller, name='Test Mebel', price=100, code='123456', species=self.species, model='Test Model', isSelling=True)
        self.order_item = OrderItem.objects.create(count=1, object=self.mebel, user=self.user)
        self.order = Order.objects.create(user=self.user)
