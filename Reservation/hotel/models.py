from django.db import models
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    isRegistered = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    checkInDate = models.DateField()
    checkOutDate = models.DateField()
    numGuests = models.IntegerField()
    status = models.CharField(max_length=50)

class Room(models.Model):
    pricePerNight = models.FloatField()
    capacity = models.IntegerField()
    availability = models.BooleanField(default=True)
class Complaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.content
class Response(models.Model):
    complaint = models.OneToOneField(Complaint, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    def __str__(self):
        return self.content