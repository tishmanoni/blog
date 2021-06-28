from django import forms
from .models import Mypost


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)



class PostForm(forms.ModelForm):
    class Meta:
        model = Mypost
        fields = ('title', 'image', 'detail', 'files', )