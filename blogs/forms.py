from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, post

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(max_length=137, required=True)


    class Meta: 
        model = User
        fields = ('username','first_name','last_name','email','password1','password2',)



class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']