from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField,UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, ProfileUser


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Логин',widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    password = forms.CharField(label='Пароль',widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    error_messages = {
        'invalid_login':('Не верный лониг или пароль')
    }

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Ваше имя',widget=forms.TextInput(attrs={
        'class':'form-control'}))
    last_name = forms.CharField(label='Ваше фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    email = forms.EmailField(label='Ваша почта',widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    username = UsernameField(label='Придумайте логин', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password1 = forms.CharField(label='Придумайте пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Потдвердите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password1','password2')

class CommentForm(forms.ModelForm):
    text = forms.CharField(
        label='Оставить комментарий',
        widget=forms.Textarea(attrs={
            'class': 'form-control text-light border-0 shadow-sm rounded-4 p-3',
            'placeholder': 'Напишите свой комментарий...',
            'rows': 4,
            'style': (
                'resize:none; font-size:16px; transition:box-shadow 0.3s ease; '
                'background-color: rgba(0,0,0,0.3);' 
            ),
            'onfocus': "this.style.boxShadow='0 0 10px rgba(255,255,255,0.3)'",
            'onblur': "this.style.boxShadow='none'"
        })
    )



    class Meta:
        model = Comment
        fields = ('text',)

class EditAccountForm(forms.ModelForm):
    first_name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    last_name = forms.CharField(label='Ваше фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control'}))
    email = forms.EmailField(label='Ваша почта', widget=forms.EmailInput(attrs={
        'class': 'form-control'
    }))
    username = UsernameField(label='Придумайте логин', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    old_password = forms.CharField(required=False,label='Текущий пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    new_password = forms.CharField(required=False,min_length=8,label='Новый пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))
    new_password2 = forms.CharField(required=False,min_length=8,label='Потвдердить пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'old_password', 'new_password','new_password2')

class EditProfileUserForm(forms.ModelForm):
    location = forms.CharField(label='Место локации',required=False,max_length=50,widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    about = forms.CharField(
        label='О себе',
        required=False,
        max_length=300,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'style': (
                'background-color: transparent; '
                'color: white; '
                'border: 1px solid rgba(255,255,255,0.4); '
                'transition: all 0.3s ease; '
            ),
            'onmouseover': "this.style.backgroundColor='rgba(255,255,255,0.1)'",
            'onmouseout': "this.style.backgroundColor='transparent'",
        })
    )
    photo = forms.ImageField(label='Фото',required=False,widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = ProfileUser
        fields = ('location','photo','about')

