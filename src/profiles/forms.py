from django import forms
from accounts.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['status', 'about']