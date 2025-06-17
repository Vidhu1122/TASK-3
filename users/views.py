from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import login
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from courses.models import Course


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

@login_required
def dashboard_view(request):
    print(f"Logged in user: {request.user.username}, role: {request.user.role}")
    courses = Course.objects.all()
    return render(request, 'users/dashboard.html', {
        'courses': courses
    })



def dummy_payment_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'users/payment.html', {'course': course})
