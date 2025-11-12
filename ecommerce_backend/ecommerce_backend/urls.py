from django.contrib import admin
from django.urls import path, include
from ecommerce_backend.api.router import router
from graphene_django.views import GraphQLView
from ecommerce_backend.schema import schema
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/users/', include('users.urls')),
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
    path('api/v1/', include('orders.urls')),
    
  
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
