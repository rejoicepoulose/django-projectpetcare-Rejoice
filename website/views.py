from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    login as auth_login,
    logout
)
from .models import (
    Pet,
    Notification,
    AdoptionRequest,
    GroomingBooking,
    Feedback,
    Message
)
from .forms import (
    RegisterForm,
    AdoptionRequestForm,
    GroomingBookingForm,
    FeedbackForm,
    MessageForm
)


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def pet_list(request):

    search = request.GET.get('search')

    age = request.GET.get('age')

    pets = Pet.objects.all()

    if search:

        pets = pets.filter(
             name__icontains=search
        ) | Pet.objects.filter(
            breed__icontains=search
        ) | Pet.objects.filter(
            location__icontains=search
        ) | Pet.objects.filter(
            species__icontains=search
        ) | Pet.objects.filter(
            temperament__icontains=search
    )

    if age:

        pets = pets.filter(
            age=age
        )

    return render(
        request,
        'pets.html',
        {
            'pets': pets
        }
    )
def services(request):
    return render(request, 'services.html')


def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

    else:

        form = RegisterForm()

    return render(
        request,
        'register.html',
        {
            'form': form
        }
    )
def login(request):

    message = ''

    if request.method == 'POST':

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            auth_login(request, user)

            message = 'Login Successful'

        else:

            message = 'Invalid Username or Password'

    return render(
        request,
        'login.html',
        {
            'message': message
        }
    )


def adopt_pet(request):

    success = False

    if request.method == 'POST':

        form = AdoptionRequestForm(request.POST)

        if form.is_valid():

            form.save()

            form = AdoptionRequestForm()

            success = True

    else:

        form = AdoptionRequestForm()

    return render(
        request,
        'adoption.html',
        {
            'form': form,
            'success': success
        }
    )
def book_grooming(request):

    success = False

    if request.method == 'POST':

        form = GroomingBookingForm(request.POST)

        if form.is_valid():

            form.save()

            form = GroomingBookingForm()

            success = True

        else:

            print(form.errors)

    else:

        form = GroomingBookingForm()

    return render(
        request,
        'booking.html',
        {
            'form': form,
            'success': success
        }
    )
def feedback_page(request):

    success = False

    if request.method == 'POST':

        form = FeedbackForm(request.POST)

        if form.is_valid():

            form.save()

            form = FeedbackForm()

            success = True

    else:

        form = FeedbackForm()

    return render(
        request,
        'feedback.html',
        {
            'form': form,
            'success': success
        }
    )
def notifications_page(request):

    notifications = Notification.objects.all().order_by(
        '-created_at'
    )

    return render(
        request,
        'notifications.html',
        {
            'notifications': notifications
        }
    )
def dashboard(request):

    context = {
    'user_count': User.objects.count(),
    'pet_count': Pet.objects.count(),
    'adoption_count': AdoptionRequest.objects.count(),
    'grooming_count': GroomingBooking.objects.count(),
    'feedback_count': Feedback.objects.count(),
    'notification_count': Notification.objects.count(),
    'message_count': Message.objects.count(),
}

    return render(
        request,
        'dashboard.html',
        context
    )
def logout_user(request):

    logout(request)

    return render(
        request,
        'login.html',
        {
            'message': 'Logged Out Successfully'
        }
    )
def message_page(request):

    success = False

    if request.method == 'POST':

        form = MessageForm(request.POST)

        if form.is_valid():

            form.save()

            form = MessageForm()

            success = True

    else:

        form = MessageForm()

    return render(
        request,
        'message.html',
        {
            'form': form,
            'success': success
        }
    )