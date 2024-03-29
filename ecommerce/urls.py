from django.urls import path
from .views import HomeView, AboutView, ContactView

app_name = 'ecommerce'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
