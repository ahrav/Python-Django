from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime, date, timedelta
import bcrypt
NAME_REGEX = re.compile(r'^[a-zA-Z ]*$')
# Create your models here.

class UserManager(models.Manager):
    def validate_registration(self, postData):
        errors = []
        if len(postData['name']) < 3 or len(postData['name']) == 0:
            errors.append('Name must be longer than 3 characters')
        if not NAME_REGEX.match(postData['name']):
            errors.append('Name can only contain letters')
        if self.filter(username = postData['username']):
            errors.append('username already in use')
        if len(postData['username']) < 3 or len(postData['username']) == 0:
            errors.append('Username must be longer than 3 characters')
        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        if postData['password'] != postData['password_confirm']:
            errors.append('Passwords do not match')
        return errors

    def create_user(self, cleanData):
        hashed = bcrypt.hashpw(cleanData['password'].encode(), bcrypt.gensalt())
        return self.create(
            name = cleanData['name'],
            username = cleanData['username'],
            password = hashed
        )
    def validate_login(self, postData):
        errors = []
        user = None
        if self.filter(username = postData['username']):
            user = self.get(username = postData['username'])
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors.append('Incorrect, username/password')
                user = None
        else:
            errors.append('Incorrect, username/password')
            user = None
        return errors, user


class TripManager(models.Manager):
    def validate_trip(self, postData):
        errors = []
        # travel_date_to = postData['travel_to_date']
        today = datetime.today()
        if len(postData['destination']) < 1:
            errors.append('Destination can not be empty')
        if len(postData['description']) < 1:
            errors.append('Desription can not be empty')
        try:
            travel_date_from = datetime.strptime(postData['travel_from_date'], '%Y-%m-%d')
            if travel_date_from < today - timedelta(1):
                errors.append('Travel date from can not be in the past')
            if postData['travel_to_date'] < postData['travel_from_date']:
                errors.append('Travel date to can not be before travel date from')
        except ValueError:
            errors.append('Must fill out date fields')
        return errors

    def create_trip(self, cleanData):
        return self.create(
            destination = cleanData['destination'],
            travel_start_date = cleanData['travel_from_date'],
            travel_end_date = cleanData['travel_to_date'],
            plan = cleanData['description'],
        )

    def not_organizer(self, trip_id):
        user = self.get(id=trip_id).users.all()
        return user[1:]

    def organizer(self, trip_id):
        user = self.get(id=trip_id).users.all()
        return user[0]


class Trip(models.Model):
    destination = models.CharField(max_length=255)
    travel_start_date = models.DateField()
    travel_end_date = models.DateField()
    plan = models.TextField()
    objects = TripManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'destination: {}, travel_start_date: {}, travel_end_date: {}, plan: {}'.format(self.destination, self.travel_start_date, self.travel_end_date, self.plan)


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    trips = models.ManyToManyField(Trip, related_name = "users")
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'name: {}, username: {}, password: {}, trips: {}'.format(self.name, self.username, self.password, self.trips)
