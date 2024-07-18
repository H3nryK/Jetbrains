from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .forms import *
from django.contrib.auth.decorators import login_required

def main_view(request):
    testimonies = Testimony.objects.all().order_by('-time')[:10]

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

    return render(request, 'main.html', {'testimonies':testimonies})

def enroll_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course = request.POST.get('courseCategory')
        info = request.POST.get('message')
        package = request.POST.get('course')

        enroll, created = Enrollment.objects.get_or_create(
            name = name,
            email = email,
            phone = phone,
            course = course,
            info = info,
            package = package
        )

        messages.success(request, "Thank you for Joining us.")

        return redirect('enroll')
    
    return render(request, 'enroll.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}.")
            return redirect('dashboard')
        else:
            messages.warning(request, "Sorry, this isn't your desk.")
            return redirect('login')

    else:

        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('main')

def testify_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('emial')
        course = request.POST.get('course')
        message = request.POST.get('testimony')

        testify, created = Testimony.objects.get_or_create(
            name = name,
            email = email,
            course = course,
            message = message
        )

        messages.success(request, "Thank you for sharing your experience.")

        return redirect('testify')
    
    return render(request, 'testify.html')

@login_required
def dashboard_view(request):
    testimonies = Testimony.objects.all().order_by('-time')
    enrollments = Enrollment.objects.all().order_by('-time')
    contacts = Contact.objects.all().order_by('-time')
    
    if request.method == 'POST':
        change_form = ChangePasswordForm(request.user, request.POST)
        if change_form.is_valid():
            user = change_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, f"Successfully changed your password.")
            return redirect('dashboard')
        else:
            messages.warning(request, f"Sorry, couldn't change your password.")
    else:
        change_form = ChangePasswordForm(request.user)

    return render(request, 'dashboard.html', {'testimonies':testimonies, 'enrollments':enrollments, 'change_form':change_form, 'contacts':contacts})

def approve_testimonial(request, testimonial_id):
    if request.method == 'POST':
        testimonial = get_object_or_404(Testimony, pk=testimonial_id)
        testimonial.approved = True
        testimonial.save()
        messages.success(request, "Successfully Approved")
    return redirect('dashboard')

def course_list_view(request):
    return render(request, 'course-list.html')