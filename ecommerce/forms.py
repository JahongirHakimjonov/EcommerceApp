from django import forms

from ecommerce.models import Contact


class ContactModelForm(forms.ModelForm):
    reason = forms.ChoiceField(choices=Contact.ContactChoice)

    class Meta:
        model = Contact
        fields = ['name', 'phone', 'reason', 'subject']


__all__ = ["ContactModelForm"]
