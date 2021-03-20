"""View module for handling requests about bills"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from healthybillsapi.models import bill

class Bill(ViewSet):

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            bill = Bill.objects.get(pk=pk)
            serializer = BillSerializer(bill, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        """Handle GET requests to get all bills

        Returns:
            Response -- JSON serialized list of bills
        """
        bills = Bill.objects.all()

        # Note the addtional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        serializer = BillSerializer(
            bills, many=True, context={'request': request})
        return Response(serializer.data)

class BillSerializer(serializers.HyperlinkedModelSerializer):
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
