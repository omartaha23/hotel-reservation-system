from django.contrib import admin
from .models import User, Room, Reservation, Complaint, Response
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Complaint)
admin.site.register(Response)

