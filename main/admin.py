from django.contrib import admin

from . import models

# Register your models here.
class RoomReservationAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.RoomReservation, RoomReservationAdmin)