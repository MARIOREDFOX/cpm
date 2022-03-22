from django.urls import path
from .api import MemberCreateApi, MemberApi, MemberUpdateApi, MemberDeleteApi

urlpatterns = [
    path('api',MemberApi.as_view()),
    path('api/create',MemberCreateApi.as_view()),
    path('api/<int:pk>',MemberUpdateApi.as_view()),
    path('api/<int:pk>/delete',MemberDeleteApi.as_view()),
]