# from newuser.models import usermodel
# from rest_framework import generics
# from .serializers import *
# from .models import *

# Create your views here.
# def usermodel(request):
#     if request.method=="POST":
#         firstname= request.POST.get('firstname')
#         lastname= request.POST.get('lastname')
#         email= request.POST.get('email')
#         phone= request.POST.get('phone')
#         usermodel=usermodel.objects.create(firstname=firstname, lastname=lastname, email=email,phone=phone)
#         usermodel.save()
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import employee, usermodel 
from .serializers import userserializer , employeeserializer , userEmployeeJoin
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.
@csrf_exempt
def get(request):
    if request.method=='GET':
        allUsers = usermodel.objects.all()
        serializer = userserializer(allUsers,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt        
def post(request):
    if request.method=='POST':
        receivedData = JSONParser().parse(request)
        serializer = userserializer(data=receivedData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Succesfully',safe=False)
        return JsonResponse('Failed to add',safe=False)  

@csrf_exempt
def put(request):
    if  request.method=='PUT':
        receivedData = JSONParser().parse(request)
        user1 = usermodel.objects.get(id=receivedData['id'])
        serializer = userserializer(user1,data=receivedData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Updated successfully',safe=False)
        return JsonResponse('Update failed',safe=False)     

@csrf_exempt   
def delete(request,id=0):
    if request.method=='DELETE':
        user1 = usermodel.objects.get(id=id)
        user1.delete()
        return JsonResponse('Deleted succesfully',safe=False)

@csrf_exempt 
def find(request,id=0):
    if request.method == 'GET':
        user1 = usermodel.objects.get(id=id)
        serializer = userserializer(user1)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def getEmployee(request):
    if request.method=='GET':
        allEmployee = employee.objects.all()
        serializer = employeeserializer(allUsers,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt        
def postEmployee(request):
    if request.method=='POST':
        receivedData = JSONParser().parse(request)
        serializer = employeeserializer(data=receivedData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Succesfully',safe=False)
        return JsonResponse('Failed to add',safe=False)  

@csrf_exempt
def putEmployee(request):
    if  request.method=='PUT':
        receivedData = JSONParser().parse(request)
        employee= employee.objects.get(id=receivedData['id'])
        serializer = employeeserializer(any,data=any)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Updated successfully',safe=False)
        return JsonResponse('Update failed',safe=False)     

@csrf_exempt   
def deleteEmployee(request,id=0):
    if request.method=='DELETE':
        employee= employee.objects.get(id=id)
        employee.delete()
        return JsonResponse('Deleted succesfully',safe=False)

@csrf_exempt 
def findEmployee(request,id=0):
    if request.method == 'GET':
        employee= employee.objects.get(id=id)
        serializer = employeeserializer(any)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt 
def joinUserEmployer(request):
    allusers = employee.objects.all()
    serializer = userEmployeeJoin(allusers,many=True)
    return JsonResponse(serializer.data,safe=False)        
