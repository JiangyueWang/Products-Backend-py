from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serilizer import ProductSerializer


@api_view(['GET'])
def product_list(request):
    prodcuts = Product.objects.all()
    serilizers = ProductSerializer(prodcuts, many=True)
    return Response(serilizers.data)
