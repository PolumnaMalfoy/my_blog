from django import forms

from main.models import Articles


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'content']
