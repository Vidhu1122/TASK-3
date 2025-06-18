from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from courses.models import Course
from .forms import UserRegisterForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VideoProgress
import json

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

@csrf_exempt
@login_required
def save_progress(request, course_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        last_time = data.get('last_time')
        course = Course.objects.get(id=course_id)

        progress, created = VideoProgress.objects.get_or_create(user=request.user, course=course)
        progress.last_time = last_time
        progress.save()
        return JsonResponse({'status': 'success'})

@login_required
def get_progress(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        progress = VideoProgress.objects.get(user=request.user, course=course)
        return JsonResponse({'last_time': progress.last_time})
    except VideoProgress.DoesNotExist:
        return JsonResponse({'last_time': 0.0})


@login_required
def dummy_payment_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.students.add(request.user)
        return redirect('dashboard')

    return render(request, 'users/payment.html', {'course': course})
