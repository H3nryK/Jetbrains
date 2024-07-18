from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Enrollment, Contact, Testimony
from django.contrib.auth.models import User
from io import StringIO
from django.core.management import call_command

class SuperuserCreationTestCase(TestCase):
    def test_create_superuser(self):
        out = StringIO()
        call_command('createsuperuser', interactive=False, username='testuser', email='testuser@example.com', stdout=out)
        self.assertIn('Superuser created successfully', out.getvalue())

        user_exists = User.objects.filter(username='testuser').exists()
        self.assertTrue(user_exists)

class EnrollmentModelTest(TestCase):
    def setUp(self):
        self.enrollment = Enrollment.objects.create(
            name="John Doe",
            email="john@example.com",
            phone=1234567890,
            course="Math",
            package="Basic",
            info="Needs extra help",
            time=timezone.now()
        )

    def test_enrollment_str(self):
        self.assertEqual(str(self.enrollment), self.enrollment.name)

    def test_enrollment_fields(self):
        self.assertEqual(self.enrollment.email, "john@example.com")
        self.assertEqual(self.enrollment.phone, 1234567890)

class ContactModelTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            name="Jane Doe",
            email="jane@example.com",
            phone=1234567890,
            message="I need help",
            time=timezone.now()
        )

    def test_contact_str(self):
        self.assertEqual(str(self.contact), self.contact.name)

    def test_contact_fields(self):
        self.assertEqual(self.contact.email, "jane@example.com")
        self.assertEqual(self.contact.phone, 1234567890)

class TestimonyModelTest(TestCase):
    def setUp(self):
        self.testimony = Testimony.objects.create(
            name="Jake Doe",
            email="jake@example.com",
            course="Science",
            message="Great course!",
            time=timezone.now(),
            approved=False
        )

    def test_testimony_str(self):
        self.assertEqual(str(self.testimony), self.testimony.name)

    def test_testimony_fields(self):
        self.assertEqual(self.testimony.email, "jake@example.com")
        self.assertEqual(self.testimony.course, "Science")

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.testimony = Testimony.objects.create(
            name="Jake Doe",
            email="jake@example.com",
            course="Science",
            message="Great course!",
            time=timezone.now(),
            approved=False
        )

    def test_main_view_get(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    def test_main_view_post(self):
        response = self.client.post(reverse('main'), {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'number': 1234567890,
            'message': 'I need help',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contact.objects.filter(name='Jane Doe').exists())

    def test_course_list_view(self):
        response = self.client.get(reverse('course-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course-list.html')

    def test_enroll_view_get(self):
        response = self.client.get(reverse('enroll'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'enroll.html')

    def test_enroll_view_post(self):
        response = self.client.post(reverse('enroll'), {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': 1234567890,
            'courseCategory': 'Math',
            'message': 'Needs extra help',
            'course': 'Basic',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Enrollment.objects.filter(name='John Doe').exists())

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': '12345',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('dashboard'))

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main'))

    def test_testify_view_get(self):
        response = self.client.get(reverse('testify'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'testify.html')

    def test_testify_view_post(self):
        response = self.client.post(reverse('testify'), {
            'name': 'Jake Doe',
            'email': 'jake@example.com',
            'course': 'Science',
            'testimony': 'Great course!',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Testimony.objects.filter(name='Jake Doe').exists())

    def test_dashboard_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_approve_testimonial(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('approve_testimonial', args=[self.testimony.id]))
        self.assertEqual(response.status_code, 302)
        self.testimony.refresh_from_db()
        self.assertTrue(self.testimony.approved)
