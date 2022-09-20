from rest_framework.exceptions import NotFound
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from api.v1.sayt.category.services import ctg_format
from meb.models import Category


class CategoryView(GenericAPIView):
    def get_object(self, pk):
        try:
            root = Category.objects.get(pk=pk)

        except:
            raise NotFound(f"{pk} category Not Fund")
        return root

    def get(self, requests, pk=None, *args, **kwargs):
        if pk:
            result = ctg_format(self.get.get_objects(pk))
        else:
            ctgs = Category.objects.all()
            result = [ctg_format(x) for x in ctgs]
        return Response({"nimadir ": "salom"})

    def post(self, requests, *args, **kwargs):
        pass

    def put(self, requests, pk, *args, **kwargs):
        pass

    def delate(self, requests, pk, *args, **kwargs):
        root = Category.objects.get(pk=pk)
        root.delate()
        return Response({"Success": f"{root.content} muofi karoche zor"})
