from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import ApplicantCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Applicant, Application
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import JsonResponse

Applicant = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'pennapps/index.html')

@login_required
def application(request):
    # Try to retrieve an existing application for the current user
    try:
        application = Application.objects.get(applicant=request.user)
    except Application.DoesNotExist:
        application = None

    if request.method == 'POST':

        # Extract team member emails from the form
        team_member_emails = [
            request.POST.get('team_member_1', ''),
            request.POST.get('team_member_2', ''),
            request.POST.get('team_member_3', '')
        ]

        # Validate team member emails
        invalid_emails = [email for email in team_member_emails if email and not Applicant.objects.filter(email=email).exists()]
        if invalid_emails:
            # If there are invalid emails, return to the form with an error message
            for email in invalid_emails:
                messages.error(request, f"{email} is not associated with a valid user.")
            return render(request, 'pennapps/application.html', {'application': application})

        # Extract data from request.POST
        school = request.POST.get('school')
        year = request.POST.get('year')
        major = request.POST.get('major')
        phone_number = request.POST.get('phone_number')
        birthday = request.POST.get('birthday')
        q1 = request.POST.get('q1')
        q2 = request.POST.get('q2')
        first_hackathon = request.POST.get('first_hackathon') == 'y'
        team_member_1 = request.POST.get('team_member_1', '')
        team_member_2 = request.POST.get('team_member_2', '')
        team_member_3 = request.POST.get('team_member_3', '')

        # Update or create the Application model instance with the extracted data
        application, created = Application.objects.update_or_create(
            applicant=request.user,
            defaults={
                'school': school,
                'year': year,
                'major': major,
                'phone_number': phone_number,
                'birthday': birthday,
                'q1_answer': q1,
                'q2_answer': q2,
                'first_hackathon': first_hackathon,
                'team_member_1': team_member_1,
                'team_member_2': team_member_2,
                'team_member_3': team_member_3,
            }
        )

        # Redirect after saving
        return redirect('/')

    # For a GET request, or if the form is not valid, render the form
    # Pass the existing application data to the form to pre-populate it, if it exists
    context = {
        'application': application
    }
    return render(request, 'pennapps/application.html', context)

@login_required
def logout(request):
    return render(request, 'pennapps/index.html')

def signup(request):
    return render(request, 'pennapps/signup.html')

def createUser(request):
    if request.method == "POST":
        form = ApplicantCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/login')

    return render(request,'pennapps/index.html')


