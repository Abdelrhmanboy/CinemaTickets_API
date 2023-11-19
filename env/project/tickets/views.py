import turtle
from urllib import response
from django.shortcuts import render
from django.http.response import JsonResponse
from django.urls import is_valid_path
from .serializers import *
from .models import *
#----------------------------------------------
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
#----------------------------------------------

# Create your views here.




# 1- static API response no rest no model (Static DATA)
def no_rest_model(request):
    guests = [
        {
            'id': 1,
            'name': 'zyad'
        },

        {
            'id': 2,
            'name': 'zakrya'
        }
    ]

    return JsonResponse(guests , safe=False)






# 2- model data Default django without REST
def model_data_no_rest(request):
    customer_data = Customer.objects.all()

    context = {
        'customers': list(customer_data.values()),
    } 

    return JsonResponse(context , safe=False)






# 3- REST Framework Serialization
def customerSerialization(request):
    customers = Customer.objects.all()

    serializer = CustomerSerializer(customers , many=True)

    return JsonResponse(serializer.data , safe=False)




# 3- REST Framework Serialization
def MovieSerialization(request):
    movies = Movie.objects.all()
    
    serializer = MovieSerializer( movies , many=True)

    return JsonResponse(serializer.data , safe=False)
    












# 4- REST Framework @api_view Decorator
@api_view(['GET' , 'POST'])
def MovieSerializationDecoratation(request):

    if request.method == 'GET':
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies , many=True)

        return Response(serializer.data , status=status.HTTP_200_OK)
    

    if request.method == 'POST':
       serializer = MovieSerializer(data=request.data)
       
       if serializer.is_valid():
           serializer.save()

           return Response(serializer.data , status=status.HTTP_201_CREATED)
       else:
           return Response(status=status.HTTP_400_BAD_REQUEST)














# 4.1- REST Framework @api_view Decorator more complex
@api_view(['GET' , 'PUT' , 'DELETE'])
def MovieSerializationDecoratation2(request , id):
    try:
        movie = Movie.objects.get(id=id)

    except Movie.DoesNotExist:
        return Response('NOT FOUND' , status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data , status=status.HTTP_200_OK)


    elif request.method == 'PUT':
        serializer = MovieSerializer(movie , data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        else:
            return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        movie.delete()
        return Response('CONTENT DELETED' , status=status.HTTP_204_NO_CONTENT)







