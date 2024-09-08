from django.contrib import admin
from django.urls import include, path
from api.views import CompanyViewSet,Employeeviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies',CompanyViewSet)
router.register(r'employees',Employeeviewset)


urlpatterns = [
    path('',include(router.urls)) 
   
]