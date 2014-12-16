from django import forms
from django.contrib.auth.models import User
from forum.models import Section, Topic, Message  #, UserProfile


class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('text',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('username', 'email', 'first_name', 'last_name')

