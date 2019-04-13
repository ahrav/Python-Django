from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    return render(request, 'travel/index.html')

def register(request):
    errors = User.objects.validate_registration(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/')
    else:
        new_user = User.objects.create_user(request.POST)
        request.session['id'] = new_user.id
    return redirect('/travels')

def login(request):
    results = User.objects.validate_login(request.POST)
    if results[0]:
        for error in results[0]:
            messages.error(request, error)
        return redirect('/')
    else:
        request.session['id'] = results[1].id
        return redirect('/travels')

def dashboard(request):
    context = {
        'user': User.objects.get(id=request.session['id']),
        'user_trips': User.objects.get(id=request.session['id']).trips.all(),
        'other_users': User.objects.all().exclude(id=request.session['id']),
    }
    return render(request, 'travel/dashboard.html', context)

def add(request):
    return render(request, 'travel/add_plan.html')

def add_plan(request):
    errors = Trip.objects.validate_trip(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('/travels/add')
    else:
        trip = Trip.objects.create_trip(request.POST)
        User.objects.get(id=request.session['id']).trips.add(trip)
    return redirect('/travels')

def join_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    User.objects.get(id=request.session['id']).trips.add(trip)
    return redirect('/travels')

def show_destination(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    context = {
        'destination': trip,
        'not_organizer': Trip.objects.not_organizer(trip_id),
        'organizer': Trip.objects.organizer(trip_id)
    }
    print trip.users.all().exclude(id=1)
    return render (request, 'travel/destination.html', context)

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')
