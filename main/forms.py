from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model= Book
        fields= [
            'dat', 'tim', 'num_of_hour', 'phone', 'name', 'notes'
        ]
        widgets= {
            'dat': forms.TextInput(attrs={'class': "form-control", 'type': 'date'}),
            'tim': forms.TextInput(attrs={'class': "form-control", 'type': 'time'}),
            'num_of_hour': forms.TextInput(attrs={'class': "form-control"}),
            'phone': forms.TextInput(attrs={'class': "form-control"}),
            #'author': forms.Select(attrs={'class': "form-control"}),
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'notes': forms.TextInput(attrs={'class': "form-control"}),
            #'accsepted': forms.Select(attrs={'class': "form-control"}),
            #'reson': forms.TextInput(attrs={'class': "form-control"})
        }
