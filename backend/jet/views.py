from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def main_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        message = request.POST.get('message')

        contact, created = Contact.objects.get_or_create(
            name = name,
            email = email,
            phone = phone,
            message = message
        )

        messages.success(request, "Thank you for contacting us.")

        return redirect('main')

    return render(request, 'main.html')

def course_view(request):
    return render(request, 'courses.html')

def enroll_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('course')
        info = request.POST.get('message')

        enroll, created = Enrollment.objects.get_or_create(
            name = name,
            email = email,
            phone = phone,
            course = course,
            info = info
        )

        messages.success(request, "Thank you for Joining us.")

        return redirect('enroll')
    
    return render(request, 'enroll.html')