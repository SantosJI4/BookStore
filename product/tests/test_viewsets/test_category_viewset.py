import json

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title="books", slug="books")

    def test_get_all_category(self):
        response = self.client.get(
            reverse("category-list", kwargs={"version": "v1"}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category_data = json.loads(response.content)
        
        print("Categories found:", len(category_data))
        print("Response data:", category_data)

        self.assertEqual(category_data[0]["title"], self.category.title)

    def test_create_category(self):
        data = json.dumps({"title": "technology", "slug": "technology"})

        response = self.client.post(
            reverse("category-list", kwargs={"version": "v1"}),
            data=data,
            content_type="application/json",
        )
        
        if response.status_code != status.HTTP_201_CREATED:
            print("Response status:", response.status_code)
            print("Response data:", response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title="technology")

        self.assertEqual(created_category.title, "technology")