from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from .models import Skills,Country,UserRegistration
from bdjobscreateaccount.serializers import SkillsSerializer, CountrySerializer, UserRegistrationSerializer

# Create your views here.

@api_view(['GET', 'POST'])
# @csrf_exempt
def CreateSkills(request): 
    if request.method == 'GET':
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = SkillsSerializer(data=request.POST)  # Using request.POST for form data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['PUT', 'DELETE'])
def Update_skills(request, pk):

    try:
        skills = Skills.objects.get(pk=pk)
    except Skills.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SkillsSerializer(skills)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SkillsSerializer(skills, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        skills.delete()
        return HttpResponse(status=204)
    

@api_view(['GET', 'POST'])
# @csrf_exempt
def CreateCountry(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        serializer = CountrySerializer(data=request.POST)  # Using request.POST for form data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Country added successfully"}, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@api_view(['PUT', 'DELETE'])
def Update_country(request, pk):
    
    try:
        countries = Country.objects.get(pk=pk)
    except Country.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CountrySerializer(countries)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CountrySerializer(countries, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        countries.delete()
        return HttpResponse(status=204)
    

@api_view(['GET', 'POST'])
# @csrf_exempt
def CreateUserRegistration(request):
    
    if request.method == 'GET':
        user = UserRegistration.objects.all()
        serializer = UserRegistrationSerializer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.POST)  # Using request.POST for form data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
@api_view(['PUT', 'DELETE'])
def Update_UserRegistration(request, pk):

    try:
        user = UserRegistration.objects.get(pk=pk)
    except UserRegistration.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserRegistrationSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserRegistrationSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


