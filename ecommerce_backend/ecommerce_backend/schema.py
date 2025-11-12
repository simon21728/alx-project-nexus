import graphene
from graphene_django import DjangoObjectType
from users.models import User
from products.models import Product
from orders.models import Order

# GraphQL types
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ("id", "username", "email")

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "description", "price", "stock")

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("id", "user", "products", "status", "total_price", "created_at")

# Queries
class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_products = graphene.List(ProductType)
    all_orders = graphene.List(OrderType)

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_products(root, info):
        return Product.objects.all()

    def resolve_all_orders(root, info):
        return Order.objects.all()

# Mutations (optional)
class Mutation(graphene.ObjectType):
    dummy = graphene.String()

    def resolve_dummy(root, info):
        return "This is a dummy mutation"


# Create the schema
schema = graphene.Schema(query=Query, mutation=Mutation)
