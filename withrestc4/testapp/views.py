from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from testapp.permissions import IsReadOnly,IsGETOrPatch,IsSunnyPermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
class EmployeeCRUDCBV(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #authentication_classes = [TokenAuthentication]
    authentication_classes = [JSONWebTokenAuthentication]
   # permission_classes = [IsSunnyPermission,]
    permissin_class=[IsAuthenticated]


