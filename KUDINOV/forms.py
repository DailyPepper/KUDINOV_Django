from .models import Customer
from .models import Review
from django.forms import ModelForm, TextInput


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email']

        widgets = {
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }),
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email'
            }),
        }


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['anons', 'title', 'full_text']

        widgets = {
            "anons": TextInput(attrs={
                'class': 'review_form_input',
                'placeholder': 'Name'
            }),
            "title": TextInput(attrs={
                'class': 'review_form_input',
                'placeholder': 'Title'
            }),
            "full_text": TextInput(attrs={
                'class': 'review_form_text',
                'placeholder': 'Message'
            })

        }
