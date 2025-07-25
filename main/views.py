from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .models import Room, ChatMessage
from .forms import BookingForm
from django.contrib import messages

def home(request):
    return render(request, 'main/home.html')


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') # or 'home'

def chat_view(request):
    if request.method == 'POST':
        ChatMessage.objects.create(sender=request.user.username, content=request.POST['message'])
    messages = ChatMessage.objects.all().order_by('-timestamp')[:50]
    return render(request, 'chat.html', {'messages': messages})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Room, Booking
from datetime import date

@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if not room.is_booked:
        Booking.objects.create(
            user=request.user,
            room=room,
            check_in=date.today(),
            check_out=date.today(),  # You can change this with a form
            payment_method='mpesa',  # Replace with real form data
        )
        room.is_booked = True
        room.save()

    return redirect('rooms')
from django.shortcuts import render
from .models import Room

def rooms_view(request):
    rooms = Room.objects.all()
    return render(request, 'main/rooms.html', {'rooms': rooms})
# main/views.py
from django.shortcuts import render
from .models import Booking, Room, Payment  # Assuming you have these models
from django.contrib.auth.decorators import login_required

@login_required
def payments_view(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    payments = Payment.objects.filter(booking__in=bookings)

    context = {
        'payments': payments,
        'bookings': bookings,
    }
    return render(request, 'payments.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Booking, Payment, ChatMessage, Entertainment, Resource

# main/views.py

from django.shortcuts import render
from .models import Room, Booking, ChatMessage, Payment, Resource, Entertainment

def dashboard(request):
    rooms = Room.objects.all()
    bookings = Booking.objects.all()
    payments = Payment.objects.all()
    chats = ChatMessage.objects.all()
    resources = Resource.objects.all()
    entertainment = Entertainment.objects.all()

    context = {
        'rooms': rooms,
        'bookings': bookings,
        'payments': payments,
        'chats': chats,
        'resources': resources,
        'entertainment': entertainment,
    }
    return render(request, 'main/dashboard.html', context)
from django.shortcuts import render
from .models import Resource
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def resource_list(request):
    resources = Resource.objects.all()
    context = {
        'resources': resources,
        'year': datetime.now().year,
    }
    return render(request, 'resources.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage

@login_required
def chat_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            ChatMessage.objects.create(user=request.user, text=text)
        return redirect('chat')

    messages = ChatMessage.objects.order_by('-created_at')[:100][::-1]  # show last 100 in order
    return render(request, 'chat.html', {'messages': messages})
# views.py

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Booking, Payment

@login_required
def payments_view(request):
    user = request.user
    bookings = Booking.objects.filter(user=user)
    payments = Payment.objects.filter(booking__in=bookings).order_by('-date_paid')

    context = {
        'payments': payments,
        'bookings': bookings,
        'total_paid': sum(payment.amount for payment in payments if payment.status == 'PAID'),
        'total_pending': sum(payment.amount for payment in payments if payment.status != 'PAID'),
    }
    return render(request, 'payments.html', context)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def entertainment_view(request):
    entertainment_items = [
        {"title": "Movie Night", "type": "Movie", "date": "2025-07-28", "description": "Watch the latest movie in the lounge"},
        {"title": "Game Tournament", "type": "Gaming", "date": "2025-07-30", "description": "Compete in FIFA, Mortal Kombat, and more"},
        {"title": "Karaoke Night", "type": "Music", "date": "2025-08-01", "description": "Sing your heart out with friends"},
    ]
    return render(request, 'entertainment.html', {"entertainment_items": entertainment_items})