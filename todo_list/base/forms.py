from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=False)


class SignUpForm(UserCreationForm):
    def save(self, commit=True):
        created_user = super().save(commit)
        basic_group = Group.objects.get(name="basic")
        created_user.groups.add(basic_group)
        basic_group.save()

        return created_user
