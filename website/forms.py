from django import forms
from django.contrib.auth.models import User

from .models import (
    AdoptionRequest,
    GroomingBooking,
    Feedback,
    Notification,
    Message
)


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password'
        ]


class AdoptionRequestForm(forms.ModelForm):

    class Meta:
        model = AdoptionRequest

        fields = [
            'applicant_name',
            'email',
            'phone',
            'pet',
            'message'
        ]


class GroomingBookingForm(forms.ModelForm):

    class Meta:

        model = GroomingBooking

        fields = [
            'owner_name',
            'email',
            'phone',
            'pet_name',
            'service_type',
            'booking_date'
        ]

        widgets = {
            'booking_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback

        fields = [
            'name',
            'rating',
            'review'
        ]


class NotificationForm(forms.ModelForm):

    class Meta:
        model = Notification

        fields = [
            'title',
            'message'
        ]
class MessageForm(forms.ModelForm):

    class Meta:

        model = Message

        fields = [
            'name',
            'email',
            'subject',
            'message'
        ]