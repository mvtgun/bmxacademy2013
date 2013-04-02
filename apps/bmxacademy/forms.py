from django import forms
from models import Participant, Message


class RegistrationForm(forms.ModelForm):
    accept = forms.BooleanField()
    class Meta:
        model = Participant

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message