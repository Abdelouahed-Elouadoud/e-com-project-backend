from rest_framework import serializers
from .models import Custumer , Collection , Product , Reviews

class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')

    class Meta:
        model = Custumer
        fields = ['id', 'email', 'name']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Collection
        fields =['id','titre']


class ProductSerializerr(serializers.ModelSerializer):
    collection = CollectionSerializer(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'description',
            'unit_price',
            'inventory',
            'last_update',
            'collection',
            'slug'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta :
        model=Reviews
        fields=['id','date','name','description','product']
        