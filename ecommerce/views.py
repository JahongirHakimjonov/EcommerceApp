from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from ecommerce.forms import ContactModelForm
from ecommerce.models import About, Contact


class HomeView(TemplateView):
    template_name = 'ecommerce/index.html'


class AboutView(ListView):
    template_name = 'ecommerce/about.html'
    model = About
    context_object_name = 'abouts'


class ContactView(CreateView):
    template_name = 'ecommerce/contact.html'
    model = Contact
    form_class = ContactModelForm
    success_url = reverse_lazy('shop:home')
