from django.contrib import admin

from .forms import WorkoutForm
from .models import Workout

class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'sets', 'repetitions', 'load')
    form = WorkoutForm

admin.site.register(Workout, WorkoutAdmin)