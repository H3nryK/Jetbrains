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
    path('change-psw/', change_psw_view, name='change-pwd'),
]
