from django.shortcuts import render
from rest_framework import viewsets
from c_api.models import Company,Employee
from c_api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet): #import viewsets
    queryset= Company.objects.all() #import models.py
    serializer_class=CompanySerializer # import serializers

    # clreate a url in urls.py
    
    #companies/{companyId}/emplyees ///// custom api create for employee list show based on company id///////
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer