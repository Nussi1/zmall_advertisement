from rest_framework import serializers
from .models import Category, Subcategory, Advertisement, Product, FandQ, Claim
from user.models import User


class ClaimSerializer(serializers.ModelSerializer):
	product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
	user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

	class Meta:
		model = Claim
		fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
	sub_category_id = serializers.PrimaryKeyRelatedField(queryset=Subcategory.objects.all())
	user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
	advertise = serializers.PrimaryKeyRelatedField(queryset=Advertisement.objects.all())
	location = serializers.CharField(read_only=True)
	claims = serializers.SerializerMethodField()

	class Meta:
		model = Product
		fields = ['title', 'size', 'price', 'description', 'in_stock', 'is_active', 'created', 'updated', 'like', 'location', 'sub_category_id', 'user_id', 'advertise', 'feedback', 'claims']

	def create(self, validated_data):
		advertisement = validated_data.pop('advertise')
		products = Product.objects.create(advertise=advertisement, **validated_data)
		return products

	def get_claims(self, obj):
		claims = Claim.objects.filter(product_id=obj.id)
		serializer = ClaimSerializer(claims, many=True)
		return serializer.data


class SubcategorySerializer(serializers.ModelSerializer):
	category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
	products = serializers.SerializerMethodField()

	class Meta:
		model = Subcategory
		fields = ['id', 'category_id', 'name', 'products']

	def create(self, validated_data):
		category = validated_data.pop('category_id')
		subcategory = Subcategory.objects.create(category_id=category, **validated_data)
		return subcategory

	def get_products(self, obj):
		products = Product.objects.filter(sub_category_id=obj.id)
		serializer = ProductSerializer(products, many=True)
		return serializer.data


class CategorySerializer(serializers.ModelSerializer):
	subcategories = serializers.SerializerMethodField()

	class Meta:
		model = Category
		fields = ('id', 'name', 'subcategories')

	def get_subcategories(self, obj):
		subcategories = Subcategory.objects.filter(category_id=obj.id)
		serializer = SubcategorySerializer(subcategories, many=True)
		return serializer.data


class AdvertisementSerializer(serializers.ModelSerializer):
	products = serializers.SerializerMethodField()

	class Meta:
		model = Advertisement
		fields = ['urgent', 'vip', 'is_marked', 'on_sale', 'from_date', 'to_date', 'products']

	def get_products(self, obj):
		products = Product.objects.filter(advertise=obj.id)
		serializer = ProductSerializer(products, many=True)
		return serializer.data


class FandQSerializer(serializers.ModelSerializer):

	class Meta:
		model = FandQ
		fields = "__all__"



