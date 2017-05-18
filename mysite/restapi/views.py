from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from mysite.restapi.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
        API ENDPOINT THAT ALLOWS USERS TO BE VIEWS OR EDITIED
    """
    queryset = User.objects.all.order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API ENDPOINT THAT ALLOWS GROUPS TO BE VIEW OR EDITED
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
