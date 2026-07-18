from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    temperament = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(
    upload_to='pets/',
    blank=True,
    null=True
   )
    description = models.TextField()
    status = models.CharField(max_length=20, default='Available')


    def __str__(self):
        return self.name


class AdoptionRequest(models.Model):

    applicant_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.applicant_name} - {self.pet.name}"
class GroomingBooking(models.Model):

    owner_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=15)

    pet_name = models.CharField(max_length=100)

    service_type = models.CharField(max_length=100)

    booking_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):
        return f"{self.owner_name} - {self.pet_name}"
class Feedback(models.Model):

    name = models.CharField(max_length=100)

    rating = models.IntegerField()

    review = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
class Notification(models.Model):

    title = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title
class Message(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.subject
    