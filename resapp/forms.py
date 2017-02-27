from django import forms
from .models import *

class SearchForm(forms.Form):
    keyword = forms.CharField()
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['keyword'].label = "Search by City"

class MyForm(forms.Form):
    my_field = forms.BooleanField(initial=False)
