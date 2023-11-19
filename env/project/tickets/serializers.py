from rest_framework import serializers
from .models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'





class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id' , 'name' , 'reservation']








class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
