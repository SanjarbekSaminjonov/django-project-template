from django.contrib.auth.forms import UserChangeForm as OldUserChangeForm
from django.contrib.auth.forms import UserCreationForm as OldUserCreationForm

from .models import User


class UserCreationForm(OldUserCreationForm):
    class Meta:
        model = User
        fields = ("phone_number",)


class UserChangeForm(OldUserChangeForm):
    class Meta:
        model = User
        fields = (
            "phone_number",
            "full_name",
            "extra_data",
            "is_staff",
            "is_superuser",
        )
