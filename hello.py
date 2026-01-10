import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")  # ajuste para o nome do seu projeto
django.setup()

from product.factories import ProductFactory

produtos = [ProductFactory() for _ in range(50)]
print(produtos[:5])