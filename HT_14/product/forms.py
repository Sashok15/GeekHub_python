from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(label="your name", max_length=100)
    email = forms.EmailField(label="your email", max_length=100)

