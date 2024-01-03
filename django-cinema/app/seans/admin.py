from django.contrib import admin
from .models import Cinema_Hall, Showing, Ticket, Halls_Seats
# Register your models here.
admin.site.register(Cinema_Hall)
admin.site.register(Ticket)
admin.site.register(Showing)
admin.site.register(Halls_Seats)

