from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', main_view, name="main"),
    path('enroll/', enroll_view, name='enroll'),
    path('course-list/', course_list_view, name='course-list'),

    path('desk/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),
    path('testify/', testify_view, name='testify'),

    path('sitemap/', TemplateView.as_view(template_name="sitemap.xml"), name="sitemap"),

    path('dashboard/', dashboard_view, name='dashboard'),
    path('approve_testimonial/<int:testimonial_id>/', approve_testimonial, name='approve_testimonial'),

]
