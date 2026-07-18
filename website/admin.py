from django.contrib import admin

from .models import (
    Pet,
    AdoptionRequest,
    GroomingBooking,
    Feedback,
    Notification,
    Message
)


admin.site.register(Pet)


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):

    list_display = (
        'applicant_name',
        'pet',
        'email',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
    )


@admin.register(GroomingBooking)
class GroomingBookingAdmin(admin.ModelAdmin):

    list_display = (
        'owner_name',
        'pet_name',
        'service_type',
        'booking_date',
        'status'
    )

    list_filter = (
        'status',
    )


admin.site.register(Feedback)

admin.site.register(Notification)
admin.site.register(Message)