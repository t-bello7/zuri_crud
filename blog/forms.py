from django import forms
from .models import Post, Comments
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


# Override the UserCreationForm
class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email', error_messages={'exists': 'This already exists!'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widget= {
        'username':forms.TextInput(attrs={'class':'input'}),
        }

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields =('name','body')
        widgets = {
        'name':forms.TextInput(),
        'body':forms.Textarea(),

        }
