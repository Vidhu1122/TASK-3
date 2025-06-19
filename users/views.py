from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from courses.models import Course
from .forms import UserRegisterForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import VideoProgress
from django.views.decorators.http import require_POST
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
@require_POST
def update_progress(request):
    data = json.loads(request.body)
    course_id = data.get("course_id")
    progress = data.get("progress")
    try:
        course = Course.objects.get(id=course_id)
        VideoProgress.objects.update_or_create(
            user=request.user,
            course=course,
            defaults={"progress": progress}
        )
        return JsonResponse({"status": "ok"})
    except Course.DoesNotExist:
        return JsonResponse({"error": "Course not found"}, status=404)

@login_required
def get_progress(request):
    course_id = request.GET.get("course_id")
    try:
        course = Course.objects.get(id=course_id)
        vp = VideoProgress.objects.get(user=request.user, course=course)
        return JsonResponse({"progress": vp.progress})
    except (Course.DoesNotExist, VideoProgress.DoesNotExist):
        return JsonResponse({"progress": 0})


@login_required
def dummy_payment_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.students.add(request.user)
        return redirect('dashboard')

    return render(request, 'users/payment.html', {'course': course})
