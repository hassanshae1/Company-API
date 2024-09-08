from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializers,EmployeeSerilizers
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class= CompanySerializers
    
class Employeeviewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerilizers