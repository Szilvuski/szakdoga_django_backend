from rest_framework import serializers
from PetSitterApp.models import Pets, Users, Availabilities, Reservations, Roles, Sitters, Services

class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pets
        fields=('pet_id', 'user_id', 'type', 'petName', 'age', 'chip_id', 'specialNeeds')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('user_id', 'username', 'email', 'fullname', 'role_id', 'password')

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Availabilities
        fields=('availability_id', 'sitter_id', 'startDate', 'endDate', 'status')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Roles
        fields=('role_id', 'roleName')

class SitterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sitters
        fields=('sitter_id','sitterName', 'experienceLevel', 'description', 'user_id', 'location')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reservations
        fields=('reservation_id', 'startDate', 'endDate', 'user_id', 'service_id', 'sitter_id', 'pet_id', 'status', 'totalCost')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields=('service_id', 'serviceName', 'description', 'price', 'duration', 'petType')
