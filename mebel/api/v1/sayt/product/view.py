from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from api.v1.sayt.product.services import prod_format
from meb.models import ProductImg, Product
from .serializer import CategorySerializer


class ProductView(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    def get_object(self, pk):
        try:
            root = Product.objects.get(pk=pk)

        except:
            raise NotFound(f"{pk} category Not Fund")
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = prod_format(self.get.get_objects(pk))
        else:
            ctgs = Product.objects.all()
            result = [prod_format(x) for x in ctgs]
        return Response({"nimadir ": "salom"})

    def post(self, requests, *args, **kwargs):
        data=requests.data

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        data=serializer.create(validated_data=serializer.data)
        return  Response(prod_format(data))
    def put(self, requests, pk, *args, **kwargs):
        root=self.get_object(pk)
        data=requests.data

        serializer = self.serializer_class(data=data,instance=root,partial=True)
        serializer.is_valid(raise_exception=True)
        data=serializer.save()
        return  Response(prod_format(data))
    def delate(self, requests, pk, *args, **kwargs):
        root = Product.objects.get(pk=pk)
        root.delate()
        return Response({"Success": f"{root.content} muofi karoche zor"})
