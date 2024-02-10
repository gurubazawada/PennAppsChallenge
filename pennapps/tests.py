from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Application, Applicant
from django.urls import reverse


class ApplicationViewTest(TestCase):

    def setUp(self):
        self.user = Applicant.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_application_view_status_code(self):
        response = self.client.get(reverse('application')) 
        self.assertEqual(response.status_code, 200)

    def test_application_view_uses_correct_template(self):
        response = self.client.get(reverse('application'))
        self.assertTemplateUsed(response, 'pennapps/application.html')

class ApplicantModelTest(TestCase):

    def test_applicant_creation(self):
        User = get_user_model()
        user = Applicant.objects.create_user(username='testuser', password='12345')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_penn_student)
        self.assertEqual(user.username, 'testuser')

class ApplicationModelTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = Applicant.objects.create_user(username='testuser', password='12345')

    def test_application_creation(self):
        application = Application.objects.create(applicant=self.user, school='Test School')
        self.assertEqual(application.applicant, self.user)
        self.assertEqual(application.school, 'Test School')
        self.assertEqual(application.status, 'PROC')  # Default status


class ApplicationViewTest(TestCase):

    def setUp(self):
        self.user = Applicant.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_application_view_status_code(self):
        response = self.client.get(reverse('application')) 
        self.assertEqual(response.status_code, 200)

    def test_application_view_uses_correct_template(self):
        response = self.client.get(reverse('application'))
        self.assertTemplateUsed(response, 'pennapps/application.html')

class ApplicationFormTest(TestCase):

    def setUp(self):
        self.user = Applicant.objects.create_user(username='testuser', email='testuser@example.com', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_valid_form_submission(self):
        form_data = {
            'school': 'Test School',
            'year': 'fr',
            'major': 'Test Major',
            'phone_number': '123-456-7890',
            'birthday': '2000-01-01',
            'q1': 'Test Answer 1',
            'q2': 'Test Answer 2',
            'first_hackathon': 'y',
            'team_member_1': '',  
            'team_member_2': '',
            'team_member_3': '',
        }
        response = self.client.post(reverse('application'), form_data)
        self.assertEqual(response.status_code, 302)  # Assuming redirection after successful form submission

    def test_form_submission_with_invalid_team_member_email(self):
        form_data = {
            # Same as above, but with an invalid team member email
            'team_member_1': 'invalid_email@example.com',
        }
        response = self.client.post(reverse('application'), form_data)
        self.assertEqual(response.status_code, 200)  # Stays on the same page due to error

