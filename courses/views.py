from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm


@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)  # ✅ include request.FILES
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('dashboard')
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})



def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from courses.models import Course

@login_required
def dashboard_view(request):
    user = request.user

    # Show all courses to students
    if user.role == 'student':
        courses = Course.objects.all()
    else:
        # Show only instructor's courses
        courses = Course.objects.filter(instructor=user)

    return render(request, 'courses/dashboard.html', {'courses': courses})