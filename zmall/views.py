from zmall.models import Category, Subcategory, Advertisement, Product, FandQ, Claim
from zmall.serializers import CategorySerializer, SubcategorySerializer, AdvertisementSerializer, ProductSerializer, FandQSerializer, ClaimSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.gis.geos import Point

point = Point(42.8746, 74.5698)


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name')


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class SubcategoryCreateView(generics.CreateAPIView):
    serializer_class = SubcategorySerializer


class SubcategoryListView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    search_fields = ('name')


class SubcategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()


class AdvertisementCreateView(generics.CreateAPIView):
    serializer_class = AdvertisementSerializer


class AdvertisementListView(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class AdvertisementDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    my_model = Product(location=point)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class FandQCreateView(generics.CreateAPIView):
    serializer_class = FandQSerializer


class FandQListView(generics.ListAPIView):
    queryset = FandQ.objects.all()
    serializer_class = FandQSerializer


class FandQDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FandQSerializer
    queryset = FandQ.objects.all()


class ClaimCreateView(generics.CreateAPIView):
    serializer_class = ClaimSerializer


class ClaimListView(generics.ListAPIView):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer


class ClaimDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ClaimSerializer
    queryset = Claim.objects.all()
