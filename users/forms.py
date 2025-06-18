from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
import re

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'role', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError("Email already in use.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        pattern = r'^[6-9]\d{9}$'
        if not re.match(pattern, phone):
            raise ValidationError("Enter a valid 10-digit Indian mobile number.")
        return phone

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', password):
            raise ValidationError("Password must include at least one uppercase letter.")
        if not re.search(r'[a-z]', password):
            raise ValidationError("Password must include at least one lowercase letter.")
        if not re.search(r'[0-9]', password):
            raise ValidationError("Password must include at least one number.")
        if not re.search(r'[\@\$\!\%\*\?&]', password):
            raise ValidationError("Password must include at least one special character (@, $, !, %, *, ?, &).")
        return password
