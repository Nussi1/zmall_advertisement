from django.urls import path
from django.urls import path, include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from websocket.views import MessageSendAPIView


urlpatterns = [
	path("category/", include([
		path('', views.CategoryListView.as_view(), name='category'),
		path('add/', views.CategoryCreateView.as_view(), name='category-add'),
		path('detail/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
	])),
	path("subcategory/", include([
		path('', views.SubcategoryListView.as_view(), name='subcategory'),
		path('add/', views.SubcategoryCreateView.as_view(), name='subcategory-add'),
		path('detail/<int:pk>', views.SubcategoryDetailView.as_view(), name='subcategory-detail'),
	])),
	path("ad/", include([
		path('', views.AdvertisementListView.as_view(), name='ad'),
		path('add/', views.AdvertisementCreateView.as_view(), name='ad-add'),
		path('detail/<int:pk>', views.AdvertisementDetailView.as_view(), name='ad-detail'),
	])),
	path("product/", include([
		path('', views.ProductListView.as_view()),
		path('add/', views.ProductCreateView.as_view()),
		path('detail/<int:pk>', views.ProductDetailView.as_view()),
	])),
	path("fq/", include([
		path('', views.FandQListView.as_view(), name='fq'),
		path('add/', views.FandQCreateView.as_view(), name='fq-add'),
		path('detail/<int:pk>', views.FandQDetailView.as_view(), name='fq-detail'),
	])),
	path("claim/", include([
		path('', views.ClaimListView.as_view()),
		path('add/', views.ClaimCreateView.as_view()),
		path('detail/<int:pk>', views.ClaimDetailView.as_view()),
	])),
	path('message/', MessageSendAPIView.as_view()),


]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
