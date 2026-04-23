from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend

# from rest_framework.views import APIView

# from django.shortcuts import get_object_or_404

from .models import Custumer ,Collection ,Product , Reviews
from .serializers import ProductSerializer ,ProductSerializerr, CollectionSerializer , ReviewSerializer

# from rest_framework.generics import ListCreateAPIView

from rest_framework.viewsets import ModelViewSet

from .filters import ProductFilter

from rest_framework.filters import SearchFilter , OrderingFilter

from rest_framework.pagination import PageNumberPagination
# Create your views here.

def home(request):
    customers = Custumer.objects.all()[:3] 
    return render(request, 'home.html' , {'customers': customers})

# class products_List(APIView):
#     def get(self,request):
#         queryset= Product.objects.select_related('collection').all()[:10]
#         serializer=ProductSerializerr(
#             queryset,many=True,context={'request':request}
#         )
#         return Response(serializer.data)
#     def post(self,request):
#         serializer= ProductSerializerr(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('collection').all()
    serializer_class = ProductSerializerr
    filter_backends= [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class =ProductFilter
    search_fields = ['title','description']
    ordering_fields= ['unit_price','last_update ']

    def get_serializer_context(self):
        return {'request': self.request}

# @api_view(['GET','POST','DELETE'])  
# def products_List(request):
#     if request.method == 'GET':
#         queryset =  Custumer.objects.all()[:14]
#         serializer = ProductSerializer(queryset,many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         # serializer.validated_data
#         return Response(serializer.data,status=status.HTTP_201_CREATED)


# @api_view()
# def products_details(request, id):
#     # try:
#     #     custumer = Custumer.objects.get(pk=id)
#     #     serializer = ProductSerializer(custumer)
#     #     return Response(serializer.data)
#     # except Custumer.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND)
    
#     #or we can do
    
#     custumer = get_object_or_404(Custumer,pk=id)
#     serializer = ProductSerializer(custumer)
#     return Response(serializer.data)
    


# @api_view(['GET','POST'])
# def getCollections(request):
#     if request.method=='GET':
#         collections = Collection.objects.all()
#         serializer = CollectionSerializer(collections,many=True)
#         return Response(serializer.data)
#     elif request.method=='POST':
#         serializer=CollectionSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
# class getCollectionss(ListCreateAPIView):
#     queryset = Collection.objects.all()
#     serializer_class=CollectionSerializer

#     def get_serializer_context(self):
#         return {'request':self.request}
    

class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_serializer_context(self):
        return {'request': self.request}

class ReviewViewSet(ModelViewSet):
    serializer_class=ReviewSerializer

    def get_queryset(self):
        return Reviews.objects.filter(product_id=self.kwargs['product_pk'])

    def perform_create(self, serializer):
        serializer.save(product_id=self.kwargs['product_pk'])