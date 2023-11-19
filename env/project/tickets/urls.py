from django.urls import include , path
from . import views


urlpatterns = [
    # 1- no rest no model way (Static)
    path('DjangoNoRest/', views.no_rest_model),


    # 2- Django model data no rest
    path('DjangoModelNoRest/', views.model_data_no_rest),


    # 3- REST Framework
    path('RESTserialization/', views.customerSerialization),
    path('RESTserialization2/', views.MovieSerialization),


    # 4- REST Framework @api_view Decorator ['GET' , 'POST']
    path('RESTdecorators/' , views.MovieSerializationDecoratation),


    # 4.1- REST Framework @api_view Decorator more complex ['GET' , 'PUT' , 'DELETE']
    path('RESTdecorators2/<int:id>' , views.MovieSerializationDecoratation2),
]
