from django.db import models

# Create your models here.
class User(models.Model):
	usertype=models.CharField(max_length=100)
	name=models.CharField(max_length=100)
	email=models.EmailField()
	pswd=models.CharField(max_length=10)

	def __str__(self):
		return self.name+" - "+self.usertype

class Mobile(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	mobile_brand=models.CharField(max_length=20)
	mobile_model=models.CharField(max_length=20)
	mobile_ram=models.CharField(max_length=10)
	mobile_storage=models.CharField(max_length=10)
	mobile_price=models.IntegerField()
	mobile_image=models.ImageField(blank=True,null=True,upload_to='images/')

	def __str__(self):
		return self.mobile_brand+" - "+self.mobile_model+" - "+str(self.mobile_price)