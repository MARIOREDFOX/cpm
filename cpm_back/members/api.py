from rest_framework import generics
from rest_framework.response import Response
from .serializers import MemberSerializer
from .models import Member

class MemberCreateApi(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberApi(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDeleteApi(generics.DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer