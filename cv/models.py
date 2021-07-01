from django.db import models

class customer(models.Model):


	Firstname = models.CharField(max_length=250)
	Lastname =models.CharField(max_length=250)
	email=models.EmailField(max_length=254)
	dateofbirth=models.DateTimeField(auto_now_add=True)
	phonenumber=models.TextField(max_length=250)
	address=models.CharField(max_length=250)
	city=models.CharField(max_length=250)
	country=models.CharField(max_length=250)



class experts(models.Model):
	Firstname = models.CharField(max_length=250)
	Lastname =models.CharField(max_length=250)
	email=models.EmailField(max_length=254)
	address=models.CharField(max_length=250)
	city=models.CharField(max_length=250)
	country=models.CharField(max_length=250)
	levelofstudy=models.CharField(max_length=250)

	
	