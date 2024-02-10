from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Applicant(AbstractUser):
    is_penn_student = models.BooleanField(default=False)

class Application(models.Model):
    STATUS_CHOICES = [
        ("ACPT", "Accepted"),
        ("RJCT", "Rejected"),
        ("WLST", "Waitlisted"),
        ("PROC", "Processing"),
    ]
    YEAR_CHOICES = [
        ("nth", "9th Grade"),
        ("ten", "10th Grade"),
        ("ele", "11th Grade"),
        ("twl", "12th Grade"),
        ("fr", "Freshman"),
        ("so", "Sophomore"),
        ("ju", "Junior"),
        ("se", "Senior"),
        ("gr", "Grad"),
    ]
    FIRST_HACKATHON_CHOICES = [
        ("y", "Yes"),
        ("n", "No"),
    ]

    applicant = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='application')
    status = models.CharField(max_length=4, choices=STATUS_CHOICES, default="PROC")
    school = models.CharField(max_length=255, blank=True, null=True)
    year = models.CharField(max_length=3, choices=YEAR_CHOICES, blank=True, null=True)
    major = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Assuming standard US phone format
    birthday = models.DateField(blank=True, null=True)
    q1_answer = models.TextField(max_length=150, blank=True, null=True)  # Assuming max 150 words as per template
    q2_answer = models.TextField(max_length=150, blank=True, null=True)  
    first_hackathon = models.CharField(max_length=1, choices=FIRST_HACKATHON_CHOICES, blank=True, null=True)
    team_member_1 = models.EmailField(blank=True, null=True)
    team_member_2 = models.EmailField(blank=True, null=True)
    team_member_3 = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.applicant.username}'s Application - Status: {self.get_status_display()}"
    
