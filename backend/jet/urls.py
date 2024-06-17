from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name="main"),
    path('courses/', course_view, name='courses'),
    path('enroll/', enroll_view, name='enroll'),

    path('desk/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('testify/', testify_view, name='testify'),

    path('dashboard/', dashboard_view, name='dashboard'),
    path('approve_testimonial/<int:testimonial_id>/', approve_testimonial, name='approve_testimonial'),
]
