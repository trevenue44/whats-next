from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for field in self.fields.keys():
            self.fields[
                field
            ].help_text = (
                f"<span class='text-gray-400'>{self.fields[field].help_text}</span>"
            )

        self.helper = FormHelper()

        self.helper.label_class = "text-blue-100 block text-sm font-bold my-2"


class UserAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()

        self.helper.label_class = "text-blue-100 block text-sm font-bold my-2"
