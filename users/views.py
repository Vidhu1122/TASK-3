from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from courses.models import Course  # make sure you import Course



from django.shortcuts import render

def home_view(request):
    return render(request, 'users/home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

@login_required
def dashboard_view(request):
    courses = Course.objects.all()  # Or filter based on the user
    return render(request, 'users/dashboard.html', {'courses': courses})

@login_required
def dummy_payment_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'users/payment.html', {'course': course})

