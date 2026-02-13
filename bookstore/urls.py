"""bookstore URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from bookstore import views
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from django.http import HttpResponse

def home_view(request):
    html = """
    <h1>🎉 BookStore API está funcionando!</h1>
    <p>Bem-vindo ao BookStore API no PythonAnywhere</p>
    <h3>Endpoints disponíveis:</h3>
    <ul>
        <li><a href="/admin/">/admin/</a> - Painel administrativo</li>
        <li><a href="/hello/">/hello/</a> - Hello World</li>
        <li>/bookstore/v1/ - API v1 (orders e products)</li>
        <li>/bookstore/v2/ - API v2 (orders e products)</li>
        <li>/api-token-auth/ - Autenticação por token</li>
    </ul>
    """
    return HttpResponse(html)

urlpatterns = [
    path("", home_view, name="home"),  # URL raiz
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),
]