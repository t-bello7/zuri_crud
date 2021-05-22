from django import forms
from .models import Comments


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields =('name','body')
        widgets = {
        'name':forms.TextInput(),
        'body':forms.Textarea(),}