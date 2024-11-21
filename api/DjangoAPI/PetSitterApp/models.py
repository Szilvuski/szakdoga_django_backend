from django.db import models

class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    roleName = models.CharField(max_length=255)

    def __str__(self):
        return self.roleName

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    role_id = models.IntegerField()
    password = models.CharField(max_length=255)  # Store hashed password

    def __str__(self):
        return self.username
    
class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    serviceName = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50)
    petType = models.CharField(max_length=100)

    def __str__(self):
        return self.serviceName
    
class Sitters(models.Model):
    sitter_id = models.AutoField(primary_key=True)
    sitterName = models.CharField(max_length=255)
    experienceLevel = models.CharField(max_length=100)
    description = models.TextField()
    user_id = models.IntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.sitterName


class Pets(models.Model):
    pet_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    type = models.CharField(max_length=100)
    petName = models.CharField(max_length=100)
    age = models.IntegerField()
    chip_id = models.CharField(max_length=15, unique=True)
    specialNeeds = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.petName
    
class Availabilities(models.Model):
    availability_id = models.AutoField(primary_key=True)
    sitter_id = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Availability {self.availability_id}"
    
class Reservations(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    startDate = models.DateField()
    endDate = models.DateField()
    user_id = models.IntegerField()
    service_id = models.IntegerField()
    sitter_id = models.IntegerField()
    pet_id = models.IntegerField()
    status = models.CharField(max_length=50)
    totalCost = models.IntegerField()

    def __str__(self):
        return f"Reservation {self.reservation_id}"
    

    

    

    
