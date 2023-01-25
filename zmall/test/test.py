from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from ..models import Category, Subcategory, Advertisement, FandQ

User = get_user_model()


class TestCategoryView(APITestCase):

    def setUp(self):
        self.category_url = reverse('category')
        self.user1 = User.objects.create_user(username='userone', email='test@example.com', password='password')
        self.client.force_authenticate(user=self.user1)

    def test_category_GET_request(self):
        Category.objects.create(name='CategoryOne')
        response = self.client.get(self.category_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        url = reverse('category-add')
        payload = {'name': 'clothes'}
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], payload['name'])

    def test_update_category(self):
        category = Category.objects.create(name='CategoryOne')
        url = reverse('category-detail', kwargs={'pk': category.id})
        payload = {'name': 'Changed'}
        response = self.client.put(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], payload['name'])

    def test_delete_category(self):
        category = Category.objects.create(name='CategoryOne')
        url = reverse('category-detail', kwargs={'pk': category.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)


class TestSubcategoryView(APITestCase):

    def setUp(self):
        self.subcategory_url = reverse('subcategory')
        self.user1 = User.objects.create(username='userone', email="juliana@dev.io", password="some_pass")
        self.category = Category.objects.create(name='CategoryOne')

    def test_subcategory_GET_request(self):
        self.client.force_authenticate(user=self.user1)
        subcat = Subcategory.objects.create(category_id=self.category, name='SubcategoryOne')
        request = self.client.get(self.subcategory_url)
        self.assertEqual(subcat.name, 'SubcategoryOne')
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_create_subcategory(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('subcategory-add')
        payload = {
            'name': 'clothes',
            'category_id': self.category.id
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_subcategory(self):
        self.client.force_authenticate(user=self.user1)
        subcat = Subcategory.objects.create(category_id=self.category, name='SubcategoryOne')
        url = reverse('subcategory-detail', kwargs={'pk': subcat.id})
        payload = {
            'name': 'Changed',
            'category_id': self.category.id
        }
        response = self.client.put(url, payload)
        subcat.refresh_from_db()
        self.assertEqual(subcat.name, 'Changed')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subcategory(self):
        self.client.force_authenticate(user=self.user1)
        subcat = Subcategory.objects.create(category_id=self.category, name='SubcategoryOne')
        url = reverse('subcategory-detail', kwargs={'pk': subcat.id})
        response = self.client.delete(url)
        self.assertEqual(Subcategory.objects.count(), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestAdvertisementView(APITestCase):

    def setUp(self):
        self.advertisement_url = reverse('ad')
        self.user1 = User(email="juliana@dev.io", password="some_pass")
        self.user1.save()

    def test_advertisement_GET_request(self):
        self.client.force_authenticate(user=self.user1)
        ad = Advertisement(urgent=True, vip=True, is_marked='red', on_sale=True)
        ad.save()
        request = self.client.get(self.advertisement_url)
        self.assertEqual(ad.urgent, True)
        self.assertEqual(ad.vip, True)
        self.assertEqual(ad.is_marked, 'red')
        self.assertEqual(ad.on_sale, True)
        self.assertEqual(request.status_code, status.HTTP_200_OK)

    def test_create_advertisement(self):
        self.client.force_authenticate(user=self.user1)
        url = reverse('ad-add')
        payload = {
            'urgent': True,
            'vip': True,
            'is_marked': 'blue',
            'on_sale': True
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_PUT_request(self):
        self.client.force_authenticate(user=self.user1)
        advertisement = Advertisement.objects.create(urgent=True, vip=True, is_marked='red', on_sale=True)
        url = reverse('ad-detail', kwargs={'pk': advertisement.pk})
        payload = {
            'urgent': False,
            'vip': False,
            'is_marked': 'blue',
            'on_sale': False,
        }
        response = self.client.put(url, payload)
        updated_ad = Advertisement.objects.get(pk=advertisement.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_ad.urgent, False)
        self.assertEqual(updated_ad.vip, False)
        self.assertEqual(updated_ad.is_marked, 'blue')
        self.assertEqual(updated_ad.on_sale, False)

    def test_DELETE_request(self):
        self.client.force_authenticate(user=self.user1)
        advertisement = Advertisement.objects.create(urgent=True, vip=True, is_marked='red', on_sale=True)
        url = reverse('ad-detail', kwargs={'pk': advertisement.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Advertisement.objects.count(), 0)


class TestFandQView(APITestCase):

    def setUp(self):
        self.fq_url = reverse('fq')
        self.user1 = User.objects.create_user(username='userone', email='test@example.com', password='password')
        self.client.force_authenticate(user=self.user1)

    def test_fq_GET_request(self):
        FandQ.objects.create(title='How to...')
        response = self.client.get(self.fq_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_fq(self):
        url = reverse('fq-add')
        payload = {
            'title': 'How to...',
            'description': 'Open acc'
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], payload['title'])

    def test_update_fq(self):
        fq = FandQ.objects.create(title='How to...')
        url = reverse('fq-detail', kwargs={'pk': fq.id})
        payload = {
            'title': 'Changed',
            'description': 'Open acc'
        }
        response = self.client.put(url, payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], payload['title'])

    def test_delete_fq(self):
        fq = FandQ.objects.create(title='How to...')
        url = reverse('fq-detail', kwargs={'pk': fq.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FandQ.objects.count(), 0)


