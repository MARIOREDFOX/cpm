from django.shortcuts import render
from .serializers import MemberSerializer 
from rest_framework import viewsets      
from .models import Member                 

class MemberView(viewsets.ModelViewSet):  
    serializer_class = MemberSerializer   
    queryset = Member.objects.all()