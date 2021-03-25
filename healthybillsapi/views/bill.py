"""View module for handling requests about bills"""
from django.http import HttpResponseServerError
from rest_framework.decorators import action
from django.db.models import Sum
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import serializers
from healthybillsapi.models import Bill

class BillSerializer(serializers.ModelSerializer):
    """JSON serializer for bills

    Arguments:
        serializers
    """
    class Meta:
        model = Bill
        url = serializers.HyperlinkedIdentityField(
            view_name='bill',
            lookup_field='id'
        )
        fields = ('id', 'user', 'provider', 'bill_date', 'acct_number', 'name_on_acct', 'amount', 'least_amount')
        depth = 1
        
class BillViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    @action(detail=False)
    def sum_bill_amounts(self, requests):
        return Response(Bill.objects.all().aggregate(Sum('amount')))

    @action(detail=False)
    def sum_least_amounts(self, requests):
        return Response(Bill.objects.all().aggregate(Sum('least_amount')))
