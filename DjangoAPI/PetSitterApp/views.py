from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.http import JsonResponse
from django.db.models import Max
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError

from PetSitterApp.models import Pets, Users, Availabilities, Reservations, Roles, Sitters, Services
from PetSitterApp.serializers import PetSerializer, UserSerializer, AvailabilitySerializer, RoleSerializer, SitterSerializer, ReservationSerializer, ServiceSerializer

from django.core.files.storage import default_storage

# Create your views here.


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def availabilityApi(request, id=0):
    if request.method =='GET':
        if id!=0:
            try:
                availability=Availabilities.objects.get(availability_id=id)
                availability_serializer = AvailabilitySerializer(availability)
                return JsonResponse(availability_serializer.data, safe=False)
            except Availabilities.DoesNotExist:
                return JsonResponse({'error': 'Availability with the given ID is not found.'}, status=404)
        else:
            availabilities = Availabilities.objects.all()
            availabilities_serializer = AvailabilitySerializer(availabilities, many=True)
            return JsonResponse(availabilities_serializer.data, safe =False)
    elif request.method =='POST':
        availabilities_data = JSONParser().parse(request)
        availabilities_serializer=AvailabilitySerializer(data=availabilities_data)
        if availabilities_serializer.is_valid():
            availabilities_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe = False)
    elif request.method=='PUT':
        availabilities_data=JSONParser().parse(request)
        try:            
            availability=Availabilities.objects.get(availability_id=availabilities_data['availability_id'])
            availabilities_serializer=AvailabilitySerializer(availability, data=availabilities_data)
            if availabilities_serializer.is_valid():
                availabilities_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to update", safe=False)
        except Availabilities.DoesNotExist:
            return JsonResponse({'error': 'Availability with the given ID is not found.'}, status=404)
    elif request.method =='DELETE':
        try:            
            availability=Availabilities.objects.get(availability_id=id)
            availability.delete()
            return JsonResponse("Deleted successfully", safe = False)
        except Availabilities.DoesNotExist:
            return JsonResponse({'error': 'Availability not found.'}, status=404)
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def sitterApi(request, id=0):
    if request.method =='GET':
        if id != 0:
            try:
                sitter=Sitters.objects.get(sitter_id=id)
                sitter_data = {
                    "sitterName": sitter.sitterName,
                    "description": sitter.description,
                    "location": sitter.location
                }
                return JsonResponse(sitter_data, safe=False)
            except Sitters.DoesNotExist:
                return JsonResponse({'error': 'Sitter with the given ID is not found.'}, status=404)
        else:
            sitters = Sitters.objects.all()
            sitters_data = [
                {"sitterName": sitter.sitterName, "description": sitter.description, "location": sitter.location}
                for sitter in sitters
            ]
            return JsonResponse(sitters_data, safe =False)
    elif request.method =='POST':
        sitters_data = JSONParser().parse(request)
        sitters_serializer=SitterSerializer(data=sitters_data)
        if sitters_serializer.is_valid():
            sitters_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe = False)
    elif request.method=='PUT':
        sitters_data=JSONParser().parse(request)
        try:            
            sitter=Sitters.objects.get(sitter_id=sitters_data['sitter_id'])
            sitters_serializer=SitterSerializer(sitter, data=sitters_data)
            if sitters_serializer.is_valid():
                sitters_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to update", safe=False)
        except Sitters.DoesNotExist:
            return JsonResponse({'error': 'Sitter with the given ID is not found.'}, status=404)
    elif request.method =='DELETE':
        try:            
            sitter=Sitters.objects.get(sitter_id=id)
            sitter.delete()
            return JsonResponse("Deleted successfully", safe = False)
        except Sitters.DoesNotExist:
            return JsonResponse({'error': 'Sitter not found.'}, status=404)
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def serviceApi(request, id=0):
    if request.method =='GET':
        if id!=0:
            try:
                service=Services.objects.get(service_id=id)
                service_serializer = ServiceSerializer(service)
                return JsonResponse(service_serializer.data, safe=False)
            except Services.DoesNotExist:
                return JsonResponse({'error': 'Service with the given ID is not found.'}, status=404)
        else:
            services = Services.objects.all()
            services_serializer = ServiceSerializer(services, many=True)
            return JsonResponse(services_serializer.data, safe =False)
    elif request.method =='POST':
        services_data = JSONParser().parse(request)
        services_serializer=ServiceSerializer(data=services_data)
        if services_serializer.is_valid():
            services_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe = False)
    elif request.method=='PUT':
        services_data=JSONParser().parse(request)
        try:            
            service=Services.objects.get(service_id=services_data['service_id'])
            services_serializer=ServiceSerializer(service, data=services_data)
            if services_serializer.is_valid():
                services_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to update", safe=False)
        except Services.DoesNotExist:
            return JsonResponse({'error': 'Service with the given ID is not found.'}, status=404)
    elif request.method =='DELETE':
        try:            
            service=Services.objects.get(service_id=id)
            service.delete()
            return JsonResponse("Deleted successfully", safe = False)
        except Services.DoesNotExist:
            return JsonResponse({'error': 'Service not found.'}, status=404)
        

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def roleApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            try:
                role = Roles.objects.get(role_id=id)
                role_serializer = RoleSerializer(role)
                return JsonResponse(role_serializer.data, safe=False)
            except Roles.DoesNotExist:
                return JsonResponse({'error': 'Role with the given ID is not found.'}, status=404)
        else:
            roles = Roles.objects.all()
            roles_serializer = RoleSerializer(roles, many=True)
            return JsonResponse(roles_serializer.data, safe=False)
    elif request.method == 'POST':
        roles_data = JSONParser().parse(request)
        roles_serializer = RoleSerializer(data=roles_data)
        if roles_serializer.is_valid():
            roles_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        roles_data = JSONParser().parse(request)
        try:
            role = Roles.objects.get(role_id=roles_data['role_id'])
            roles_serializer = RoleSerializer(role, data=roles_data)
            if roles_serializer.is_valid():
                roles_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to update", safe=False)
        except Roles.DoesNotExist:
            return JsonResponse({'error': 'Role with the given ID is not found.'}, status=404)
    elif request.method == 'DELETE':
        try:
            role = Roles.objects.get(role_id=id)
            role.delete()
            return JsonResponse("Deleted successfully", safe=False)
        except Roles.DoesNotExist:
            return JsonResponse({'error': 'Role not found.'}, status=404)
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def petApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            try:
                pet = Pets.objects.get(pet_id=id)
                pet_serializer = PetSerializer(pet)
                return JsonResponse(pet_serializer.data, safe=False)
            except Pets.DoesNotExist:
                return JsonResponse({'error': 'Pet with the given ID is not found.'}, status=404)
        else:
            pets = Pets.objects.all()
            pets_serializer = PetSerializer(pets, many=True)
            return JsonResponse(pets_serializer.data, safe=False)
    elif request.method == 'POST':
        pets_data = JSONParser().parse(request)
        pets_serializer = PetSerializer(data=pets_data)
        if pets_serializer.is_valid():
            pets_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        pets_data = JSONParser().parse(request)
        try:
            pet = Pets.objects.get(pet_id=pets_data['pet_id'])
            pets_serializer = PetSerializer(pet, data=pets_data)
            if pets_serializer.is_valid():
                pets_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to update", safe=False)
        except Pets.DoesNotExist:
            return JsonResponse({'error': 'Pet with the given ID is not found.'}, status=404)
    elif request.method == 'DELETE':
        try:
            pet = Pets.objects.get(pet_id=id)
            pet.delete()
            return JsonResponse("Deleted successfully", safe=False)
        except Pets.DoesNotExist:
            return JsonResponse({'error': 'Pet not found.'}, status=404)
        

@api_view(['GET', 'PUT'])
def userApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            try:
                user = Users.objects.get(user_id=id)
                user_serializer = UserSerializer(user)
                return JsonResponse(user_serializer.data, safe=False)
            except Users.DoesNotExist:
                return JsonResponse({'error': 'User with the given ID is not found.'}, status=404)
        else:
            users = Users.objects.all()
            users_serializer = UserSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False) 
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        try:
            user = Users.objects.get(user_id=user_data['user_id'])
            user_serializer = UserSerializer(user, data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to update", safe=False)
        except Users.DoesNotExist:
            return JsonResponse({'error': 'User with the given ID is not found.'}, status=404)
        
@api_view(['POST'])
def register(request):
    try:
        users_data = JSONParser().parse(request)
        max_user_id = Users.objects.aggregate(Max('user_id'))['user_id__max'] or 0
        new_user_id = max_user_id + 1

        new_user_data = {
            "user_id": new_user_id,
            "username": users_data['username'],
            "email": users_data['email'],
            "fullname": users_data['fullname'],
            "role_id": 2,  # Default role for customer
            "password": make_password(users_data['password']),
        }

        users_serializer = UserSerializer(data=new_user_data)
        if users_serializer.is_valid(raise_exception=True):
            users_serializer.save()
            return JsonResponse({"message": "User registered successfully!"}, status=201)
    except IntegrityError:
        return JsonResponse({"error": "Username or email already exists!"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
@api_view(['POST'])
def login(request):
    try:
        data = JSONParser().parse(request)
        email = data.get('email')
        password = data.get('password')

        user = Users.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            request.session['user_id'] = user.user_id
            return JsonResponse({"message": "Sikeres bejelentkezés!", "user_id": user.user_id}, status=200)
        else:
            return JsonResponse({"error": "Érvénytelen e-mail cím vagy jelszó!"}, status=401)
    except Exception as e:
        return JsonResponse({"error": f"Hiba történt: {str(e)}"}, status=500)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def reservationApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            try:
                reservation = Reservations.objects.get(reservation_id=id)
                reservation_serializer = ReservationSerializer(reservation)
                return JsonResponse(reservation_serializer.data, safe=False)
            except Reservations.DoesNotExist:
                return JsonResponse({'error': 'Reservation with the given ID is not found.'}, status=404)
        else:
            reservations = Reservations.objects.all()
            reservations_serializer = ReservationSerializer(reservations, many=True)
            return JsonResponse(reservations_serializer.data, safe=False)
    elif request.method == 'POST':
        reservations_data = JSONParser().parse(request)
        reservations_serializer = ReservationSerializer(data=reservations_data)
        if reservations_serializer.is_valid():
            reservations_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        reservations_data = JSONParser().parse(request)
        try:
            reservation = Reservations.objects.get(reservation_id=reservations_data['reservation_id'])
            reservations_serializer = ReservationSerializer(reservation, data=reservations_data)
            if reservations_serializer.is_valid():
                reservations_serializer.save()
                return JsonResponse("Updated successfully", safe=False)
            return JsonResponse("Failed to update", safe=False)
        except Reservations.DoesNotExist:
            return JsonResponse({'error': 'Reservation with the given ID is not found.'}, status=404)
    elif request.method == 'DELETE':
        try:
            reservation = Reservations.objects.get(reservation_id=id)
            reservation.delete()
            return JsonResponse("Deleted successfully", safe=False)
        except Reservations.DoesNotExist:
            return JsonResponse({'error': 'Reservation not found.'}, status=404)
        

@api_view
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
