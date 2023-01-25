from django.db import models
from django.contrib.gis.db import models
from config import settings
from django_resized import ResizedImageField


class Category(models.Model):
	name = models.CharField(max_length=50)


class Subcategory(models.Model):
	category_id = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategory')
	name = models.CharField(max_length=100)


class Product(models.Model):
	title = models.CharField(max_length=255)
	size = models.IntegerField()
	price = models.IntegerField()
	description = models.TextField()
	in_stock = models.BooleanField()
	is_active = models.BooleanField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	like = models.BooleanField()
	location = models.PointField(null=True)
	sub_category_id = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
	user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	advertise = models.ForeignKey('Advertisement', on_delete=models.CASCADE)
	feedback = models.TextField()


class Advertisement(models.Model):
	urgent = models.BooleanField()
	vip = models.BooleanField()
	CHOICES = (
		('red', 'red'),
		('blue', 'blue'),
		('green', 'green'),
		('yellow', 'yellow')
	)
	is_marked = models.CharField(max_length=255, choices=CHOICES)
	on_sale = models.BooleanField()
	from_date = models.DateTimeField(auto_now=True)
	to_date = models.DateTimeField(auto_now=True)


class IP(models.Model):
	ip = models.IntegerField()


class SeenBy(models.Model):
	ip_id = models.ForeignKey('IP', on_delete=models.CASCADE)
	product_id = models.ForeignKey('Product', on_delete=models.CASCADE)


class Image(models.Model):
	image = ResizedImageField(upload_to='images/', quality=85)
	product_id = models.ForeignKey('Product', on_delete=models.CASCADE)


class FandQ(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()


class Contact(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField()
	title = models.CharField(max_length=255)
	content = models.TextField()


class ChatRoom(models.Model):
	product_id = models.ForeignKey('Product', on_delete=models.CASCADE)


class Chat(models.Model):
	text = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	chat_id = models.ForeignKey('ChatRoom', on_delete=models.CASCADE)
	user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Claim(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	product_id = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='claims')
	user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
