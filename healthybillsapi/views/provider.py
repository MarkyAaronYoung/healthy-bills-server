"""View module for handling requests about bills"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from healthybillsapi.models import Provider

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for bills

    Arguments:
        serializers
    """
    class Meta:
        model = Provider
        url = serializers.HyperlinkedIdentityField(
            view_name='provider',
            lookup_field='id'
        )   
        fields = ('id', 'provider_name', 'contact_number')

class ProviderViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
