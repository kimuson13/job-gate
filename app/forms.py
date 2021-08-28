from django import forms
from multiselectfield.forms.fields import MultiSelectFormField

class PostForm(forms.Form):
    title = forms.CharField(max_length=30, label='タイトル')
    content = forms.CharField(label='内容', widget=forms.Textarea())

class PostUserInfoForm(forms.Form):
    name = forms.CharField(max_length=255, label="Name")
    email = forms.EmailField()

class PostElementary(forms.Form):
    question1 = forms.CharField()
    question2 = forms.CharField()
    question3 = forms.CharField()
    question4 = forms.CharField()
    question5 = forms.CharField()