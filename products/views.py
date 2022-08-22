from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from products.serilizer import ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        prodcuts = Product.objects.all()
        serilizers = ProductSerializer(prodcuts, many=True)
        return Response(serilizers.data)
    elif request.method == 'POST':
        serilizers = ProductSerializer(data=request.data)
        if serilizers.is_valid() == True:
            serilizers.save()
            return Response(serilizers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serilizers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_details(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serilizers = ProductSerializer(product)
        return Response(serilizers.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
