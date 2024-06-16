from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name="main"),
    path('courses/', course_view, name='courses'),
    path('enroll/', enroll_view, name='enroll'),
]
