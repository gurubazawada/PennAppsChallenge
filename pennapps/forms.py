from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Applicant

class ApplicantCreationForm(UserCreationForm):
    class Meta:
        model = Applicant
        fields = UserCreationForm.Meta.fields + ('is_penn_student',)
