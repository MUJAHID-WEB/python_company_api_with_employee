from django.contrib import admin
from django.urls import path,include
from c_api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers 


router= routers.DefaultRouter() # import routers from rest_framework
router.register(r'companies', CompanyViewSet) # register viewset with urls and include
router.register(r'employees', EmployeeViewSet)

urlpatterns = [    
    path('',include(router.urls))
      
]

#let's register this app in settings and include this urls in base urls.py
#
#companies/{companyId}/employees