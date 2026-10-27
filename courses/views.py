from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Course, Enrollment


def course_list(request):
    courses = Course.objects.filter(status=Course.STATUS_APPROVED).prefetch_related('enrollments')
    enrolled_course_ids = set()
    if request.user.is_authenticated:
        enrolled_course_ids = set(
            Enrollment.objects.filter(student=request.user).values_list('course_id', flat=True)
        )
    context = {
        'courses': courses,
        'enrolled_course_ids': enrolled_course_ids,
    }
    return render(request, 'courses/course_list.html', context)


@login_required
def enroll_course(request, course_id):
    if request.method != 'POST':
        return redirect('course_list')
    course = get_object_or_404(Course, pk=course_id, status=Course.STATUS_APPROVED)
    if Enrollment.objects.filter(student=request.user, course=course).exists():
        messages.warning(request, '你已經加選過這門課程。')
        return redirect('course_list')
    if course.enrolled_count >= course.capacity:
        messages.error(request, '此課程已額滿，無法加選。')
        return redirect('course_list')
    Enrollment.objects.create(student=request.user, course=course)
    messages.success(request, f'已成功加選「{course.name}」。')
    return redirect('course_list')


@login_required
def drop_course(request, course_id):
    if request.method != 'POST':
        return redirect('my_schedule')
    enrollment = get_object_or_404(Enrollment, student=request.user, course_id=course_id)
    course_name = enrollment.course.name
    enrollment.delete()
    messages.success(request, f'已成功退選「{course_name}」。')
    return redirect('my_schedule')


@login_required
def my_schedule(request):
    enrollments = (
        Enrollment.objects.filter(student=request.user)
        .select_related('course')
        .order_by('course__schedule', 'course__code')
    )
    return render(request, 'courses/my_schedule.html', {'enrollments': enrollments})
