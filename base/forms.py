from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["name", "username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        placeholders = {
            "name": "Enter your full name",
            "username": "Choose a username",
            "email": "Enter your email",
            "password1": "••••••••",
            "password2": "••••••••",
        }

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "placeholder": placeholders.get(field, ""),
                    "autocomplete": "off",
                    "class": "form-control",
                }
            )


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = "__all__"
        exclude = ["host", "participants"]

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)

        placeholders = {
            "name": "Enter room name",
            "description": "Describe your room",
            "topic": "Choose a topic",
        }

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "placeholder": placeholders.get(field, ""),
                    "autocomplete": "off",
                    "class": "form-control",
                }
            )


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["avatar", "name", "username", "email", "bio"]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        placeholders = {
            "avatar": "Upload a profile picture",
            "name": "Enter your full name",
            "username": "Choose a username",
            "email": "Enter your email",
            "bio": "Write something about yourself",
        }

        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    "placeholder": placeholders.get(field, ""),
                    "autocomplete": "off",
                    "class": "form-control",
                }
            )
