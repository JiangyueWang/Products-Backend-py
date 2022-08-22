from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from products.models import Product
from products.serilizer import ProductSerializer


@api_view(['GET'])
def product_list(request):
    prodcuts = Product.objects.all()
    serilizers = ProductSerializer(prodcuts, many=True)
    return Response(serilizers.data)


@api_view(['GET'])
def product_details(requst, pk):
    try:
        product = Product.objects.get(pk=pk)
        serilizers = ProductSerializer(product)
        return Response(serilizers.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
