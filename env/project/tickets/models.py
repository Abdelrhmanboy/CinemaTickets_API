from django.db import models

# Create your models here.

# Cinema Tickets System:                                                            
#____________________________________________________________________________________
# Customer: name                                                                    #
# --------------------------------------------------------------------------------- #
# Movie: Title                                                                      #
# --------------------------------------------------------------------------------- #
# Ticket: forign-key(Customer)  _  forign-key(Movie)  _  seat_no  _  hall  _  price #




class Customer(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name







class Movie(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title






class Ticket(models.Model):
    customer = models.ForeignKey(Customer, related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='reservation', on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    hall_name = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.customer} Ticket"
