from django import forms
from . models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(max_length=30, label='First Name', widget=forms.TextInput(attrs={'class':'first'}))
#     last_name = forms.CharField(max_length=30, label='Last Name', widget=forms.TextInput(attrs={'class':'last'}))
#     email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class':'email'}))
#     review = forms.CharField(label='Please Review', widget=forms.Textarea(attrs={'class':'review', 'rows':'2', 'cols':'2'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "first_name":"FIRST NAME:",
            "last_name":"LAST NAME:",
            "stars":"STARS:",
        }
        error_messages = {
            'stars':{
                'max_value':'Maximum value is 5',
                'min_value': 'Minimum value is 0',
            }
        }